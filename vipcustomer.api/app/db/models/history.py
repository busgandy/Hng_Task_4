from sqlmodel import Field, JSON, Column
import uuid as uuid_pkg
from .common import TimestampModel, UUIDModel


class History(TimestampModel, UUIDModel, table=True):
    __tablename__ = "history"

    input: str = Field(sa_column=Column(JSON))
    result_id: uuid_pkg.UUID = Field(foreign_key="people.id")
    user_id: uuid_pkg.UUID = Field(foreign_key="users.id")

    class Config:
        arbitrary_types_allowed = True

    def __repr__(self):
        return f"<History (id: {self.id})>"
