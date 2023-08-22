from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from starlette import status

from app.db import get_session
from app.pastes.models import Paste
from app.pastes.service import generate_slug_from_id

router = APIRouter(
    prefix="/pastes",
    tags=["pastes"],
)


@router.get("/", description="Returns list of all pastes")
async def pastes_list(session: Session = Depends(get_session)) -> list[Paste]:
    return session.exec(select(Paste)).all()


@router.get("/{slug}", description="Returns list of all pastes")
async def paste_detail(slug: str, session: Session = Depends(get_session)) -> Paste:
    paste = session.exec(select(Paste).where(Paste.slug == slug)).first()
    if paste:
        return paste
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/")
async def add_paste(paste: Paste, session: Session = Depends(get_session)) -> Paste:
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
