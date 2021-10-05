import typing
from dataclasses import dataclass
from .text_entity import _TextEntity
from .base_class import BaseClass
from ..utils import raw_textentities_to_types


@dataclass
class HelpDocument(BaseClass):
    """
    A help document (e.g. terms of service, privacy policy, community guidelines)

    **Members:**

    - **id**: ID of the help document
    - **text**: Text of the help document
    - **entities**: The text entities
    """

    id: str
    text: str
    entities: typing.List[_TextEntity]

    @classmethod
    def from_json(cls, resp: dict):
        return cls(
            resp["id"], resp["text"], raw_textentities_to_types(resp["entities"])
        )
