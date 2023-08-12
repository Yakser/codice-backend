from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field


class UUIDBaseModel(SQLModel):
    """
    Base class for UUID-based models.
    """

    uuid: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
