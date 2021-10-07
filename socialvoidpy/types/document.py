import typing
import datetime
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

    - **id**: Document ID
    - **file_mime**: The file's mime/media type
    - **file_name**: The file name
    - **file_size**: The file size in bytes
    - **file_type**: A [`FileType`](#filetype)
    - **flags**: Flags set for the document
    - **created**: When the document was created (removed in 1.0.0.1)
    """

    id: str
    file_mime: str
    file_name: str
    file_size: int
    file_type: FileType
    flags: typing.List[str]
    created: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, resp: dict):
        if "created_timestamp" in resp:
            created = datetime.datetime.fromtimestamp(resp["created_timestamp"])
        else:
            created = None
        return cls(
            resp["id"],
            resp["file_mime"],
            resp["file_name"],
            resp["file_size"],
            FileType(resp["file_type"]),
            resp["flags"],
            created,
        )
