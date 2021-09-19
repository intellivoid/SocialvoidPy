import datetime
from dataclasses import dataclass
from .base_class import BaseClass


@dataclass
class Document(BaseClass):
    id: str
    file_mime: str
    file_name: str
    file_size: int
    file_type: str
    flags: list[str]
    created: datetime.datetime

    @classmethod
    def from_json(cls, resp: dict):
        return cls(
            resp["id"],
            resp["file_mime"],
            resp["file_name"],
            resp["file_size"],
            resp["file_type"],
            resp["flags"],
            datetime.datetime.fromtimestamp(resp["created"]),
        )
