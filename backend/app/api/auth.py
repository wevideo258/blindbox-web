from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import create_access_token
from app.db.session import get_db
from app.models import User
from app.schemas import LoginRequest, SmsRequest, TokenOut, UserOut

router = APIRouter(prefix="/auth", tags=["auth"])

_sms_store: dict[str, str] = {}


@router.post("/sms")
def send_sms(payload: SmsRequest):
    _sms_store[payload.mobile] = settings.demo_sms_code
    return {"ok": True, "message": "验证码已发送", "demo_code": settings.demo_sms_code}


@router.post("/login", response_model=TokenOut)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    expected = _sms_store.get(payload.mobile, settings.demo_sms_code)
    if payload.code != expected:
        raise HTTPException(status_code=400, detail="验证码错误")

    user = db.query(User).filter(User.mobile == payload.mobile).one_or_none()
    if user is None:
        user = User(mobile=payload.mobile, nickname=f"玩家{payload.mobile[-4:]}")
        db.add(user)
        db.commit()
        db.refresh(user)

    token = create_access_token(str(user.id))
    return TokenOut(access_token=token, user=UserOut.model_validate(user))
