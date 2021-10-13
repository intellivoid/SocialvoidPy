import typing
from dataclasses import dataclass
from .display_picture_size import DisplayPictureSize
from .base_class import BaseClass


@dataclass
class Profile(BaseClass):
    """
    A profile

    **Members:**

    - **first_name** (`str`): The first name of the entity
    - **last_name** (`str`, `None`): The optional last name of the entity
    - **name** (`str`): The full display name of the entity
    - **biography** (`str`): The optional biography or description of the entity
    - **url** (`str`, `None`): The optional URL of the entity
    - **followers_count** (`int`): The amount of followers this entity has
    - **following_count** (`int`): The amount of peers this entity is following
    - **display_picture_sizes** ([`DisplayPictureSize[]`](#displaypicturesize)): An array of display pictures of this entity
    """

    first_name: str
    last_name: typing.Optional[str]
    name: str
    biography: typing.Optional[str]
    url: typing.Optional[str]
    followers_count: int
    following_count: int
    display_picture_sizes: typing.List[DisplayPictureSize]

    @classmethod
    def from_json(cls, resp: dict):
        return cls(
            resp["first_name"],
            resp["last_name"],
            resp["name"],
            resp["biography"],
            resp["url"],
            resp["followers_count"],
            resp["following_count"],
            [DisplayPictureSize.from_json(i) for i in resp["display_picture_sizes"]],
        )
