from dataclasses import dataclass
from .display_picture_size import DisplayPictureSize
from .base_class import BaseClass


@dataclass
class Peer(BaseClass):
    id: str
    type: str
    name: str
    username: str
    display_picture_sizes: list[DisplayPictureSize]
    flags: list[str]

    @classmethod
    def from_json(cls, resp: dict):
        return cls(
            resp["id"],
            resp["type"],
            resp["name"],
            resp["username"],
            [DisplayPictureSize.from_json(i) for i in resp["display_picture_sizes"]],
            resp["flags"],
        )
