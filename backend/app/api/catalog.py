from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload

from app.db.session import get_db
from app.deps import get_current_user
from app.models import BlindBox, DrawRecord, User
from app.schemas import BoxOut, UserOut

router = APIRouter(tags=["users"])


@router.get("/users/me", response_model=UserOut)
def me(user: User = Depends(get_current_user)):
    return user


@router.get("/boxes", response_model=list[BoxOut])
def list_boxes(db: Session = Depends(get_db)):
    boxes = db.query(BlindBox).options(selectinload(BlindBox.prizes)).filter(BlindBox.is_active.is_(True)).all()
    return boxes


@router.get("/boxes/{box_id}", response_model=BoxOut)
def get_box(box_id: int, db: Session = Depends(get_db)):
    box = db.query(BlindBox).options(selectinload(BlindBox.prizes)).filter(BlindBox.id == box_id).one_or_none()
    if box is None:
        raise HTTPException(status_code=404, detail="盲盒不存在")
    return box


@router.get("/broadcast")
def broadcast(db: Session = Depends(get_db)):
    records = (
        db.query(DrawRecord)
        .order_by(DrawRecord.id.desc())
        .limit(9)
        .all()
    )
    items = []
    for record in records:
        prize = record.prize
        user = record.user
        items.append(
            {
                "user_name": user.nickname,
                "prize": prize.full_name,
                "time": "刚刚",
                "is_blue": prize.is_jackpot,
            }
        )
    if not items:
        items = [
            {"user_name": "ShiJieBok", "prize": "iPhone 17 (128GB)", "time": "刚刚", "is_blue": True},
            {"user_name": "月光收藏家", "prize": "Nintendo Switch OLED 版", "time": "1分钟前", "is_blue": True},
            {"user_name": "潮玩新手", "prize": "未抽中 · 等额余额返还", "time": "3分钟前", "is_blue": False},
        ]
    return items
