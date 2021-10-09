import typing
from dataclasses import dataclass, field
from .base_class import BaseClass


@dataclass
class _TextEntity(BaseClass):
    offset: int
    length: int
    value: typing.Optional[str]
    type: str
    value_required: bool = field(default=False, init=False, repr=False)

    def __post_init__(self):
        if self.value is None and self.value_required:
            raise ValueError("value must not be None")

    @classmethod
    def from_json(cls, resp: dict):
        return cls(resp["offset"], resp["length"], resp["value"], resp["type"])


@dataclass
class BoldTextEntity(_TextEntity):
    """
    A bold text entity

    **Members:**

    - **offset**: Offset into the text
    - **length**: Length of the entity
    - **value**: An optional value (e.g. a url for URLTextEntity)
    """

    value: typing.Optional[str] = None
    type: str = field(default="BOLD", repr=False)


@dataclass
class ItalicTextEntity(_TextEntity):
    """
    An italic text entity

    See [`BoldTextEntity`](#boldtextentity) for members
    """

    value: typing.Optional[str] = None
    type: str = field(default="ITALIC", repr=False)


@dataclass
class CodeTextEntity(_TextEntity):
    """
    A code text entity

    See [`BoldTextEntity`](#boldtextentity) for members
    """

    value: typing.Optional[str] = None
    type: str = field(default="CODE", repr=False)


@dataclass
class StrikeTextEntity(_TextEntity):
    """
    A strikethrough text entity

    See [`BoldTextEntity`](#boldtextentity) for members
    """

    value: typing.Optional[str] = None
    type: str = field(default="STRIKE", repr=False)


@dataclass
class UnderlineTextEntity(_TextEntity):
    """
    An underline text entity

    See [`BoldTextEntity`](#boldtextentity) for members
    """

    value: typing.Optional[str] = None
    type: str = field(default="UNDERLINE", repr=False)


@dataclass
class URLTextEntity(_TextEntity):
    """
    A URL text entity

    See [`BoldTextEntity`](#boldtextentity) for members
    """

    type: str = field(default="URL", repr=False)
    value_required: bool = field(default=True, init=False, repr=False)


@dataclass
class MentionTextEntity(_TextEntity):
    """
    A mention text entity

    See [`BoldTextEntity`](#boldtextentity) for members
    """

    type: str = field(default="MENTION", repr=False)
    value_required: bool = field(default=True, init=False, repr=False)


@dataclass
class HashtagTextEntity(_TextEntity):
    """
    A hashtag text entity

    See [`BoldTextEntity`](#boldtextentity) for members
    """

    type: str = field(default="HASHTAG", repr=False)
    value_required: bool = field(default=True, init=False, repr=False)


TEXT_ENTITY_MAP = {
    "BOLD": BoldTextEntity,
    "ITALIC": ItalicTextEntity,
    "CODE": CodeTextEntity,
    "STRIKE": StrikeTextEntity,
    "UNDERLINE": UnderlineTextEntity,
    "URL": URLTextEntity,
    "MENTION": MentionTextEntity,
    "HASHTAG": HashtagTextEntity,
}

__all__ = [
    "BoldTextEntity",
    "ItalicTextEntity",
    "CodeTextEntity",
    "StrikeTextEntity",
    "UnderlineTextEntity",
    "URLTextEntity",
    "MentionTextEntity",
    "HashtagTextEntity",
]
