from typing import Optional

from sqlmodel import Field, SQLModel


class Paste(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        index=True,
    )
    slug: str | None = Field(unique=True, index=True, nullable=True, regex=r"^[-\w]+\Z")
    author: str | None
    content: str | None
    title: str | None
    description: str | None
    # access by link
