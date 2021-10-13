import typing
from dataclasses import dataclass
from .text_entity import _TextEntity
from .base_class import BaseClass
from ..utils import raw_textentities_to_types
from ..parser import ParseMode, unparse


@dataclass
class HelpDocument(BaseClass):
    """
    A help document (e.g. terms of service, privacy policy, community guidelines)

    **Members:**

    - **id**: ID of the help document
    - **raw_text**: Raw text of the help document
    - **entities**: Text entities of the raw text
    """

    id: str
    raw_text: str
    entities: typing.List[_TextEntity]

    @classmethod
    def from_json(cls, resp: dict):
        return cls(
            resp["id"], resp["text"], raw_textentities_to_types(resp["entities"])
        )

    def get_html_text(self) -> str:
        """
        Parses the raw text and entities into an HTML string

        **Returns:** `str`
        """

        return unparse(self.raw_text, self.entities, ParseMode.HTML)
