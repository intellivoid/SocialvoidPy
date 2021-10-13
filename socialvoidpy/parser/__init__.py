import enum
import typing
from . import html
from ..types.text_entity import _TextEntity


class ParseMode(enum.Enum):
    """
    Parse mode for text and entities

    **Members:**

    - **HTML**
    """

    HTML = enum.auto()


_PARSE_FUNC_MAP = {ParseMode.HTML: (html.parse, html.unparse)}


def unparse(
    text: str, entities: typing.List[_TextEntity], parse_mode: ParseMode
) -> str:
    """
    Unparses text and entities into an encoded string

    **Parameters:**

    - **text** (`str`): Text to unparse
    - **entities** (`TextEntity[]`): Entities to unparse
    - **parse_mode** (`ParseMode`): The parse mode
    """

    return _PARSE_FUNC_MAP[parse_mode][1](text, entities)


def parse(
    text: str, parse_mode: ParseMode
) -> typing.Tuple[str, typing.List[_TextEntity]]:
    """
    Parses an encoded string into an unencoded string and its entities

    **Parameters:**

    - **text** (`str`): Text to unparse
    - **parse_mode** (`ParseMode`): The parse mode
    """

    return _PARSE_FUNC_MAP[parse_mode][0](text)
