from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from app.db import engine
from app.pastes.models import Paste
from app.pastes.service import generate_slug_from_id

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
        if session.exec(select(Paste).where(Paste.slug == paste.slug)).all():
            raise HTTPException(
                status_code=422, detail="Paste with given slug already exists!"
            )

        session.add(paste)
        session.commit()
        session.refresh(paste)
        if paste.slug is None:
            paste.slug = generate_slug_from_id(paste.id)
            session.add(paste)
            session.commit()
            session.refresh(paste)
        return paste
