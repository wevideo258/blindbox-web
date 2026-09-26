from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mobile: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    nickname: Mapped[str] = mapped_column(String(64), default="拾界玩家")
    avatar: Mapped[str] = mapped_column(String(255), default="/static/用户头像.png")
    balance: Mapped[float] = mapped_column(Float, default=88.50)
    points: Mapped[float] = mapped_column(Float, default=198.0)
    vip_level: Mapped[int] = mapped_column(Integer, default=2)
    vip_exp: Mapped[int] = mapped_column(Integer, default=99)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    draws: Mapped[list["DrawRecord"]] = relationship(back_populates="user")
    cards: Mapped[list["UserCard"]] = relationship(back_populates="user")


class BlindBox(Base):
    __tablename__ = "blind_boxes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    slug: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(128))
    subtitle: Mapped[str] = mapped_column(String(128), default="")
    price: Mapped[float] = mapped_column(Float)
    remaining: Mapped[int] = mapped_column(Integer, default=0)
    cover: Mapped[str] = mapped_column(String(255), default="/static/盲盒.png")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    prizes: Mapped[list["Prize"]] = relationship(back_populates="box")


class Prize(Base):
    __tablename__ = "prizes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    box_id: Mapped[int] = mapped_column(ForeignKey("blind_boxes.id"), index=True)
    name: Mapped[str] = mapped_column(String(64))
    full_name: Mapped[str] = mapped_column(String(128))
    image: Mapped[str] = mapped_column(String(255))
    rarity: Mapped[str] = mapped_column(String(16), default="N")
    weight: Mapped[int] = mapped_column(Integer, default=1)
    remaining: Mapped[int] = mapped_column(Integer, default=0)
    is_jackpot: Mapped[bool] = mapped_column(Boolean, default=False)
    refund_balance: Mapped[bool] = mapped_column(Boolean, default=False)
    refund_amount: Mapped[float] = mapped_column(Float, default=0)
    card_code: Mapped[str | None] = mapped_column(String(32), nullable=True)

    box: Mapped["BlindBox"] = relationship(back_populates="prizes")


class DrawRecord(Base):
    __tablename__ = "draw_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    box_id: Mapped[int] = mapped_column(ForeignKey("blind_boxes.id"), index=True)
    prize_id: Mapped[int] = mapped_column(ForeignKey("prizes.id"))
    target_prize_id: Mapped[int | None] = mapped_column(ForeignKey("prizes.id"), nullable=True)
    cost: Mapped[float] = mapped_column(Float)
    refunded: Mapped[float] = mapped_column(Float, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    user: Mapped["User"] = relationship(back_populates="draws")
    prize: Mapped["Prize"] = relationship(foreign_keys=[prize_id])


class CardSeries(Base):
    __tablename__ = "card_series"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    slug: Mapped[str] = mapped_column(String(32), unique=True)
    name: Mapped[str] = mapped_column(String(32))
    cover: Mapped[str] = mapped_column(String(255))

    cards: Mapped[list["CollectibleCard"]] = relationship(back_populates="series")


class CollectibleCard(Base):
    __tablename__ = "collectible_cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    series_id: Mapped[int] = mapped_column(ForeignKey("card_series.id"), index=True)
    code: Mapped[str] = mapped_column(String(32), unique=True)
    name: Mapped[str] = mapped_column(String(64))
    rarity: Mapped[str] = mapped_column(String(16), default="N")

    series: Mapped["CardSeries"] = relationship(back_populates="cards")


class UserCard(Base):
    __tablename__ = "user_cards"
    __table_args__ = (UniqueConstraint("user_id", "card_id"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    card_id: Mapped[int] = mapped_column(ForeignKey("collectible_cards.id"), index=True)
    count: Mapped[int] = mapped_column(Integer, default=1)

    user: Mapped["User"] = relationship(back_populates="cards")
    card: Mapped["CollectibleCard"] = relationship()
