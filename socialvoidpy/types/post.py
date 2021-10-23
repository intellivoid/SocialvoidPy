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

    - **id** (`str`): ID of the post
    - **type** ([`PostType`](#posttype)): The post type
    - **peer** ([`Peer`](#peer), `None`): The peer that sent the post
    - **source** (`str`, `None`): The source of the post determined serverside
    - **raw_text** (`str`, `None`): Raw text of the post
    - **entities** (`TextEntity[]`): Text entities of the raw text
    - **mentioned_peers** ([`Peer[]`](#peer)): Mentioned peers in the post
    - **reply_to_post** (`Post`, `None`): What this post is replying to if any
    - **quoted_post** (`Post`, `None`): What this post was quoting if any
    - **reposted_post** (`Post`, `None`): The original post if any
    - **original_thread_post** (`Post`, `None`): The original thread if any
    - **like_count** (`int`, `None`): Amount of times this post has been liked
    - **repost_count** (`int`, `None`): Amount of times this post has been reposted
    - **quote_count** (`int`, `None`): Amount of times this post has been quoted
    - **reply_count** (`int`, `None`): Amount of times this post has been replied to
    - **posted_timestamp** (`datetime.datetime`): When this post was posted
    - **flags** (`str[]`): Flags set on this post
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
    original_thread_post: typing.Optional["Post"]
    like_count: typing.Optional[int]
    repost_count: typing.Optional[int]
    quote_count: typing.Optional[int]
    reply_count: typing.Optional[int]
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
            raw_textentities_to_types(resp["entities"]),
            [Peer.from_json(i) for i in resp["mentioned_peers"]],
            Post.from_json(resp["reply_to_post"]) if resp["reply_to_post"] else None,
            Post.from_json(resp["quoted_post"]) if resp["quoted_post"] else None,
            Post.from_json(resp["reposted_post"]) if resp["reposted_post"] else None,
            Post.from_json(resp["original_thread_post"])
            if resp["original_thread_post"]
            else None,
            resp["like_count"],
            resp["repost_count"],
            resp["quote_count"],
            resp["reply_count"],
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
