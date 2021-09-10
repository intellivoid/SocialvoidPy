from dataclasses import dataclass
from .text_entity import _TextEntity
from .base_class import BaseClass
from ..utils import raw_textentities_to_types

@dataclass
class HelpDocument(BaseClass):
    id: str
    text: str
    entities: list[_TextEntity]

    @classmethod
    def from_json(cls, resp):
        return cls(resp['id'], resp['text'], raw_textentities_to_types(resp['entities']))
