from typing import Optional

from sqlmodel import Field, SQLModel


class Paste(SQLModel, table=True):
    id: str = Field(
        primary_key=True, unique=True, index=True, nullable=False, regex=r"^[-\w]+\Z"
    )
    name: Optional[str]
    text: str
