import datetime
from dataclasses import dataclass
from .base_class import BaseClass

@dataclass
class Session(BaseClass):
    id: str
    flags: list[str]
    authenticated: bool
    created: datetime.datetime
    expires: datetime.datetime

    @classmethod
    def from_json(cls, resp: dict):
        return cls(resp['id'], resp['flags'], resp['authenticated'], datetime.datetime.fromtimestamp(resp['created']), datetime.datetime.fromtimestamp(resp['expires']))
