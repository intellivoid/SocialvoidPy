import typing
import datetime
from dataclasses import dataclass
from .base_class import BaseClass


@dataclass
class Session(BaseClass):
    """
    A session

    **Members:**

    - **id** (`str`): The session's ID
    - **flags** (`str[]`): Flags set on the session
    - **authenticated** (`bool`): If the session is authenticated
    - **created** (`datetime.datetime`): When the session was created
    - **expires** (`datetime.datetime`): When the session will expire
    """

    id: str
    flags: typing.List[str]
    authenticated: bool
    created: datetime.datetime
    expires: datetime.datetime

    @classmethod
    def from_json(cls, resp: dict):
        return cls(
            resp["id"],
            resp["flags"],
            resp["authenticated"],
            datetime.datetime.fromtimestamp(resp["created"]),
            datetime.datetime.fromtimestamp(resp["expires"]),
        )
