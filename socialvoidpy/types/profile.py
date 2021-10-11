import typing
from dataclasses import dataclass
from .display_picture_size import DisplayPictureSize
from .base_class import BaseClass


@dataclass
class Profile(BaseClass):
    """
    A profile

    **Members:**

    - **first_name**: The first name of the entity
    - **last_name**: The optional last name of the entity (can be None)
    - **name**: The full display name of the entity
    - **biography**: The optional biography or description of the entity (can be None)
    - **url**: The optional URL of the entity (can be None)
    - **followers_count**: The amount of followers this entity has
    - **following_count**: The amount of peers this entity is following
    - **display_picture_sizes**: An array of display pictures of this entity
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
