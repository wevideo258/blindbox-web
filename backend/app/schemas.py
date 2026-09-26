from datetime import datetime

from pydantic import BaseModel, Field


class ApiOk(BaseModel):
    ok: bool = True


class SmsRequest(BaseModel):
    mobile: str = Field(min_length=11, max_length=11)


class LoginRequest(BaseModel):
    mobile: str = Field(min_length=11, max_length=11)
    code: str = Field(min_length=4, max_length=6)


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: "UserOut"


class UserOut(BaseModel):
    id: int
    mobile: str
    nickname: str
    avatar: str
    balance: float
    points: float
    vip_level: int
    vip_exp: int

    model_config = {"from_attributes": True}


class PrizeOut(BaseModel):
    id: int
    name: str
    full_name: str
    image: str
    rarity: str
    remaining: int
    is_jackpot: bool
    refund_balance: bool
    weight: int

    model_config = {"from_attributes": True}


class BoxOut(BaseModel):
    id: int
    slug: str
    title: str
    subtitle: str
    price: float
    remaining: int
    cover: str
    prizes: list[PrizeOut] = []

    model_config = {"from_attributes": True}


class DrawRequest(BaseModel):
    target_prize_id: int | None = None


class DrawResultOut(BaseModel):
    draw_id: int
    box_id: int
    cost: float
    refunded: float
    hit_jackpot: bool
    prize: PrizeOut
    balance: float
    created_at: datetime


class DrawRecordOut(BaseModel):
    id: int
    box_id: int
    cost: float
    refunded: float
    prize: PrizeOut
    created_at: datetime

    model_config = {"from_attributes": True}


class CardOut(BaseModel):
    id: int
    code: str
    name: str
    rarity: str
    owned: int = 0

    model_config = {"from_attributes": True}


class SeriesOut(BaseModel):
    slug: str
    name: str
    cover: str
    owned: int
    total: int
    cards: list[CardOut]


class CardProgressOut(BaseModel):
    owned: int
    total: int
    percent: float
    series: list[SeriesOut]


class BroadcastOut(BaseModel):
    user_name: str
    prize: str
    time: str
    is_blue: bool = False
