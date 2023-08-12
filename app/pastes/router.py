from fastapi import APIRouter
from sqlmodel import Session, select

from app.db import engine
from app.pastes.models import Paste

router = APIRouter(
    prefix="/pastes",
    tags=["pastes"],
)


@router.get("/", description="Returns list of all pastes")
async def pastes_list() -> list[Paste]:
    with Session(engine) as session:
        return session.exec(select(Paste)).all()


@router.post("/")
async def add_paste(paste: Paste) -> Paste:
    with Session(engine) as session:
        session.add(paste)
        session.commit()
        session.refresh(paste)
        return paste
