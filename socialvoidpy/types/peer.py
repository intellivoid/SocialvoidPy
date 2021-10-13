import typing
from enum import Enum
from dataclasses import dataclass
from .base_class import BaseClass


class PeerType(Enum):
    """
    A peer type

    **Members:**

    - **USER**: A normal user account
    - **BOT**: A bot account that performs automated actions on the network
    - **PROXY**: A proxy account that mirrors content from another platform
    """

    USER = "USER"
    BOT = "BOT"
    PROXY = "PROXY"


@dataclass
class Peer(BaseClass):
    """
    A peer (aka user)

    **Members:**

    - **id** (`str`): The peer's id
    - **type** ([`PeerType`](#peertype)): The peer's type
    - **name** (`str`): The peer's name
    - **username** (`str`): The peer's username
    - **flags** (`str[]`): Flags set for the peer
    """

    id: str
    type: PeerType
    name: str
    username: str
    flags: typing.List[str]

    @classmethod
    def from_json(cls, resp: dict):
        return cls(
            resp["id"],
            PeerType(resp["type"]),
            resp["name"],
            resp["username"],
            resp["flags"],
        )
