import typing
from enum import Enum
from dataclasses import dataclass
from .display_picture_size import DisplayPictureSize
from .base_class import BaseClass


class PeerType(Enum):
    USER = "USER"
    BOT = "BOT"
    PROXY = "PROXY"


@dataclass
class Peer(BaseClass):
    id: str
    type: PeerType
    name: str
    username: str
    display_picture_sizes: typing.List[DisplayPictureSize]
    flags: typing.List[str]

    @classmethod
    def from_json(cls, resp: dict):
        return cls(
            resp["id"],
            PeerType(resp["type"]),
            resp["name"],
            resp["username"],
            [DisplayPictureSize.from_json(i) for i in resp["display_picture_sizes"]],
            resp["flags"],
        )
