from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from starlette import status

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


@router.get("/{slug}", description="Returns list of all pastes")
async def paste_detail(slug: str) -> Paste:
    with Session(engine) as session:
        paste = session.exec(select(Paste).where(Paste.slug == slug)).first()
        if paste:
            return paste
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/")
async def add_paste(paste: Paste) -> Paste:
    with Session(engine) as session:
        if session.exec(select(Paste).where(Paste.slug == paste.slug)).all():
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Paste with given slug already exists!",
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
