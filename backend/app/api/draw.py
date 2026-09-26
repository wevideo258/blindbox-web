from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload

from app.db.session import get_db
from app.deps import get_current_user
from app.models import DrawRecord, Prize, User
from app.schemas import DrawRequest, DrawResultOut, PrizeOut
from app.services.draw import DrawError, draw_once

router = APIRouter(tags=["draw"])


@router.post("/boxes/{box_id}/draw", response_model=DrawResultOut)
def draw_box(
    box_id: int,
    payload: DrawRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    try:
        record = draw_once(db, user, box_id, payload.target_prize_id)
    except DrawError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message) from exc

    prize = db.get(Prize, record.prize_id)
    return DrawResultOut(
        draw_id=record.id,
        box_id=record.box_id,
        cost=record.cost,
        refunded=record.refunded,
        hit_jackpot=bool(prize and prize.is_jackpot),
        prize=PrizeOut.model_validate(prize),
        balance=user.balance,
        created_at=record.created_at,
    )


@router.get("/draws/me")
def my_draws(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    records = (
        db.query(DrawRecord)
        .options(selectinload(DrawRecord.prize))
        .filter(DrawRecord.user_id == user.id)
        .order_by(DrawRecord.id.desc())
        .limit(50)
        .all()
    )
    return [
        {
            "id": item.id,
            "box_id": item.box_id,
            "cost": item.cost,
            "refunded": item.refunded,
            "prize": PrizeOut.model_validate(item.prize),
            "created_at": item.created_at,
        }
        for item in records
    ]
