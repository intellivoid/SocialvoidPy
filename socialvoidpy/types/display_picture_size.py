from dataclasses import dataclass
from .document import Document
from .base_class import BaseClass


@dataclass
class DisplayPictureSize(BaseClass):
    width: int
    height: int
    document: Document

    @classmethod
    def from_json(cls, resp: dict):
        return cls(resp["width"], resp["height"], Document.from_json(resp["document"]))
