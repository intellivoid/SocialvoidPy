from dataclasses import dataclass
from .document import Document
from .base_class import BaseClass


@dataclass
class DisplayPictureSize(BaseClass):
    """
    A display/profile picture

    **Members:**

    - **width** (`int`): Width of the image
    - **height** (`int`): Height of the image
    - **document** ([`types.Document`](#document)): The document
    """

    width: int
    height: int
    document: Document

    @classmethod
    def from_json(cls, resp: dict):
        return cls(resp["width"], resp["height"], Document.from_json(resp["document"]))
