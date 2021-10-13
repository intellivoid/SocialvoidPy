import typing
from enum import Enum
from dataclasses import dataclass
from .base_class import BaseClass


class FileType(Enum):
    """
    A file type

    **Members:**

    - **DOCUMENT**
    - **PHOTO**
    - **VIDEO**
    - **AUDIO**
    """

    DOCUMENT = "DOCUMENT"
    PHOTO = "PHOTO"
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"


@dataclass
class Document(BaseClass):
    """
    A document

    **Members:**

    - **id** (`str`): Document ID
    - **file_mime** (`str`): The file's mime/media type
    - **file_name** (`str`): The file name
    - **file_size** (`int`): The file size in bytes
    - **file_type** ([`FileType`](#filetype)): The file type
    - **flags** (`str[]`): Flags set for the document
    """

    id: str
    file_mime: str
    file_name: str
    file_size: int
    file_type: FileType
    flags: typing.List[str]

    @classmethod
    def from_json(cls, resp: dict):
        return cls(
            resp["id"],
            resp["file_mime"],
            resp["file_name"],
            resp["file_size"],
            FileType(resp["file_type"]),
            resp["flags"],
        )
