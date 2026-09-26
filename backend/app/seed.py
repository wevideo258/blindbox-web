from __future__ import annotations

from sqlalchemy.orm import Session

from app.models import BlindBox, CardSeries, CollectibleCard, Prize, User


def seed_if_empty(db: Session) -> None:
    if db.query(BlindBox).first():
        return

    box = BlindBox(
        slug="digital-carnival",
        title="本期盲盒·数码狂欢",
        subtitle="抽中直接发货 · 未抽中100%返还等额余额可提现",
        price=9.9,
        remaining=328,
        cover="/static/盲盒.png",
        is_active=True,
    )
    db.add(box)
    db.flush()

    prizes = [
        Prize(
            box_id=box.id,
            name="iPhone 17",
            full_name="iPhone 17 (128GB)",
            image="/static/banaana.png",
            rarity="SSR",
            weight=8,
            remaining=3,
            is_jackpot=True,
        ),
        Prize(
            box_id=box.id,
            name="潮流球鞋",
            full_name="Nike Dunk Low 潮流限定",
            image="/static/潮版手办.png",
            rarity="SR",
            weight=20,
            remaining=12,
            is_jackpot=True,
        ),
        Prize(
            box_id=box.id,
            name="潮版手办",
            full_name="潮版手办盲盒限定手办",
            image="/static/美妆专区.png",
            rarity="SR",
            weight=30,
            remaining=20,
            is_jackpot=True,
        ),
        Prize(
            box_id=box.id,
            name="Switch",
            full_name="Nintendo Switch OLED 版",
            image="/static/数码狂欢.png",
            rarity="SSR",
            weight=10,
            remaining=6,
            is_jackpot=True,
        ),
        Prize(
            box_id=box.id,
            name="余额返还",
            full_name="未抽中 · 等额余额返还",
            image="/static/logo1.png",
            rarity="N",
            weight=932,
            remaining=287,
            is_jackpot=False,
            refund_balance=True,
            refund_amount=9.9,
            card_code="zhaocai-west",
        ),
    ]
    db.add_all(prizes)

    series_data = [
        ("zhaocai", "招财", "/static/招财图鉴.png", ["east", "west", "south", "north", "center"]),
        ("pixie", "辟邪", "/static/辟邪图鉴.png", ["mask", "bell", "seal", "sword"]),
        ("gaiyun", "改运", "/static/改运图鉴.png", ["coin", "dice", "lotus", "star"]),
        ("shenshou", "神兽", "/static/神兽图鉴.png", ["qinglong", "baihu", "zhuque", "xuanwu"]),
    ]
    for slug, name, cover, codes in series_data:
        series = CardSeries(slug=slug, name=name, cover=cover)
        db.add(series)
        db.flush()
        for code in codes:
            db.add(
                CollectibleCard(
                    series_id=series.id,
                    code=f"{slug}-{code}",
                    name=f"{name}·{code}",
                    rarity="R" if code in {"west", "qinglong"} else "N",
                )
            )

    demo = User(
        mobile="13800138000",
        nickname="ShiJieBok",
        balance=88.50,
        points=198.0,
        vip_level=2,
        vip_exp=99,
    )
    db.add(demo)
    db.commit()
