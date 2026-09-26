from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, selectinload

from app.db.session import get_db
from app.deps import get_current_user
from app.models import CardSeries, User, UserCard
from app.schemas import CardOut, CardProgressOut, SeriesOut

router = APIRouter(prefix="/cards", tags=["cards"])


@router.get("/progress", response_model=CardProgressOut)
def progress(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    owned_map = {
        item.card_id: item.count
        for item in db.query(UserCard).filter(UserCard.user_id == user.id).all()
    }
    series_rows = db.query(CardSeries).options(selectinload(CardSeries.cards)).all()

    series_out: list[SeriesOut] = []
    owned_total = 0
    all_total = 0
    for series in series_rows:
        cards = []
        owned = 0
        for card in series.cards:
            count = owned_map.get(card.id, 0)
            if count > 0:
                owned += 1
            cards.append(
                CardOut(
                    id=card.id,
                    code=card.code,
                    name=card.name,
                    rarity=card.rarity,
                    owned=count,
                )
            )
        owned_total += owned
        all_total += len(series.cards)
        series_out.append(
            SeriesOut(
                slug=series.slug,
                name=series.name,
                cover=series.cover,
                owned=owned,
                total=len(series.cards),
                cards=cards,
            )
        )

    percent = round((owned_total / all_total) * 100, 1) if all_total else 0.0
    return CardProgressOut(owned=owned_total, total=all_total, percent=percent, series=series_out)
