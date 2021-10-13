import enum
import typing
from datetime import datetime
from dataclasses import dataclass
from .peer import Peer
from .text_entity import _TextEntity
from .base_class import BaseClass
from ..utils import raw_textentities_to_types
from ..parser import ParseMode, unparse


class PostType(enum.Enum):
    """
    The post's type

    **Members:**

    - **UNKNOWN**: Unknown post type
    - **DELETED**: A deleted post
    - **POST**: An ordinary post
    - **REPLY**: A post that's in reply to another post
    - **QUOTE**: A post that quotes another post
    - **REPOST**: A repost of another post
    """

    UNKNOWN = "UNKNOWN"
    DELETED = "DELETED"
    POST = "POST"
    REPLY = "REPLY"
    QUOTE = "QUOTE"
    REPOST = "REPOST"


@dataclass
class Post(BaseClass):
    """
    A post

    **Members:**

    - **id**: ID of the post
    - **type**: The [`PostType`](#posttype)
    - **peer**: The [`Peer`](#peer) that sent the post (can be None)
    - **source**: The source of the post determined serverside (can be None)
    - **raw_text**: Raw text of the post (can be None)
    - **entities**: Text entities of the raw text
    - **mentioned_peers**: Mentioned peers in the post
    - **reply_to_post**: What this post is replying to (can be None)
    - **quoted_post**: What this post was quoting (can be None)
    - **reposted_post**: The original post (can be None)
    - **like_count**: Amount of times this post has been liked (can be None)
    - **repost_count**: Amount of times this post has been reposted (can be None)
    - **quote_count**: Amount of times this post has been quoted (can be None)
    - **posted_timestamp**: When this post was posted
    - **flags**: Flags set on this post
    """

    id: str
    type: PostType
    peer: typing.Optional[Peer]
    source: typing.Optional[str]
    raw_text: typing.Optional[str]
    entities: typing.List[_TextEntity]
    mentioned_peers: typing.List[Peer]
    reply_to_post: typing.Optional["Post"]
    quoted_post: typing.Optional["Post"]
    reposted_post: typing.Optional["Post"]
    like_count: typing.Optional[int]
    repost_count: typing.Optional[int]
    quote_count: typing.Optional[int]
    posted_timestamp: datetime
    flags: typing.List[str]

    @classmethod
    def from_json(cls, resp: dict):
        return cls(
            resp["id"],
            PostType(resp["type"]),
            Peer.from_json(resp["peer"]),
            resp["source"],
            resp["text"],
            raw_textentities_to_types(resp["entities"] or []),
            [Peer.from_json(i) for i in resp["mentioned_peers"] or []],
            Post.from_json(resp["reply_to_post"]),
            Post.from_json(resp["quoted_post"]),
            Post.from_json(resp["reposted_post"]),
            resp["likes_count"],  # intentional s because it's in the standard
            resp["reposts_count"],  # intentional s because it's in the standard
            resp["quotes_count"],  # intentional s because it's in the standard
            datetime.fromtimestamp(resp["posted_timestamp"]),
            resp["flags"],
        )

    def get_html_text(self) -> typing.Optional[str]:
        """
        Parses the raw text and entities into an HTML string (returns None if post is deleted)

        **Returns:** `str` or `None`
        """

        if self.raw_text is None:
            return None
        return unparse(self.raw_text, self.entities, ParseMode.HTML)
