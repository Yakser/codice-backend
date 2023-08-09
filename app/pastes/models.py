from fastapi import APIRouter

router = APIRouter(
    prefix="/pastes",
    tags=["pastes"],
)


@router.get("/", description="Returns list of all pastes")
async def pastes_list() -> list[str]:
    pass
