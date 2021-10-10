import typing
from enum import Enum
from dataclasses import dataclass
from .display_picture_size import DisplayPictureSize
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

    - **id**: The peer's id
    - **type**: The [`PeerType`](#peertype)
    - **name**: The peer's name
    - **username**: The peer's username
    - **display_picture_sizes**: The peer's display/profile pictures (removed in 1.0.0.1, see `network.get_profile`)
    - **flags**: Flags set for the peer
    """

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
            [
                DisplayPictureSize.from_json(i)
                for i in resp.get("display_picture_sizes", [])
            ],
            resp["flags"],
        )
