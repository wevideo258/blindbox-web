from __future__ import annotations

import secrets
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models import BlindBox, CollectibleCard, DrawRecord, Prize, User, UserCard

rng = secrets.SystemRandom()


class DrawError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


def _weighted_pick(prizes: list[Prize], target_prize_id: int | None) -> Prize:
    available = [p for p in prizes if p.remaining > 0]
    if not available:
        raise DrawError("本期奖品已抽完")

    weights: list[int] = []
    for prize in available:
        weight = max(prize.weight, 1)
        if target_prize_id and prize.id == target_prize_id and prize.is_jackpot:
            weight = int(weight * 1.35)
        weights.append(weight)

    return rng.choices(available, weights=weights, k=1)[0]


def draw_once(db: Session, user: User, box_id: int, target_prize_id: int | None) -> DrawRecord:
    box = db.execute(
        select(BlindBox).options(selectinload(BlindBox.prizes)).where(BlindBox.id == box_id)
    ).scalar_one_or_none()
    if box is None or not box.is_active:
        raise DrawError("盲盒不存在或已下架", 404)
    if box.remaining <= 0:
        raise DrawError("本期次数已用完")
    if user.balance < box.price:
        raise DrawError("余额不足")

    if target_prize_id is not None:
        target = next((p for p in box.prizes if p.id == target_prize_id), None)
        if target is None:
            raise DrawError("目标大奖不在本期奖池中")

    prize = _weighted_pick(box.prizes, target_prize_id)

    user.balance -= box.price
    refunded = 0.0
    if prize.refund_balance:
        refunded = prize.refund_amount or box.price
        user.balance += refunded

    prize.remaining -= 1
    box.remaining -= 1

    if prize.card_code:
        card = db.execute(
            select(CollectibleCard).where(CollectibleCard.code == prize.card_code)
        ).scalar_one_or_none()
        if card is not None:
            owned = db.execute(
                select(UserCard).where(UserCard.user_id == user.id, UserCard.card_id == card.id)
            ).scalar_one_or_none()
            if owned is None:
                db.add(UserCard(user_id=user.id, card_id=card.id, count=1))
            else:
                owned.count += 1

    record = DrawRecord(
        user_id=user.id,
        box_id=box.id,
        prize_id=prize.id,
        target_prize_id=target_prize_id,
        cost=box.price,
        refunded=refunded,
        created_at=datetime.now(timezone.utc),
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    db.refresh(user)
    db.refresh(prize)
    return record
