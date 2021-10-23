import typing
from .. import types
from ..utils import async_create_session_id, async_auto_create_session
from ..request import Request

if typing.TYPE_CHECKING:
    from . import AsyncSocialvoidClient


class Timeline:
    """
    `timeline` methods
    """

    def __init__(self, sv: "AsyncSocialvoidClient"):
        self._sv = sv

    @async_auto_create_session
    async def compose(
        self,
        text: str,
        attachments: typing.Sequence[typing.Union[str, types.Document]] = (),
    ) -> types.Post:
        """
        Composes a post

        **Parameters:**

        - **text** (`str`): The post's contents
        - **attachments** (`str[]`, [`types.Document[]`](/types/#document), optional): Optional attachments for the post

        **Returns:** [`types.Post`](/types/#post)

        **Authentication Required:** Yes
        """

        attachments = [
            i.id if isinstance(i, types.Document) else i for i in attachments
        ]
        resp = (
            await self._sv.make_request(
                Request(
                    "timeline.compose",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        ),
                        "text": text,
                        "attachments": attachments,
                    },
                )
            )
        ).unwrap()
        return types.Post.from_json(resp)

    @async_auto_create_session
    async def get_post(self, post: typing.Union[str, types.Post]) -> types.Post:
        """
        Fetches a post

        **Parameters:**

        - **post** (`str`, [`types.Post`](/types/#post)): The post to get

        **Authentication Required:** Yes
        """

        if isinstance(post, types.Post):
            post = post.id
        resp = (
            await self._sv.make_request(
                Request(
                    "timeline.get_post",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        ),
                        "post": post,
                    },
                )
            )
        ).unwrap()
        return types.Post.from_json(resp)

    @async_auto_create_session
    async def delete(self, post: typing.Union[str, types.Post]) -> bool:
        """
        Delete a post

        **Parameters:**

        - **post** (`str`, [`types.Post`](/types/#post)): The post to delete

        **Authentication Required:** Yes
        """

        if isinstance(post, types.Post):
            post = post.id
        return (
            await self._sv.make_request(
                Request(
                    "timeline.delete",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        ),
                        "post": post,
                    },
                )
            )
        ).unwrap()

    @async_auto_create_session
    async def like(self, post: typing.Union[str, types.Post]) -> bool:
        """
        Likes a post

        **Parameters:**

        - **post** (`str`, [`types.Post`](/types/#post)): The post to like

        **Authentication Required:** Yes
        """

        if isinstance(post, types.Post):
            post = post.id
        return (
            await self._sv.make_request(
                Request(
                    "timeline.like",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        ),
                        "post": post,
                    },
                )
            )
        ).unwrap()

    @async_auto_create_session
    async def get_feed(self, page: int = 1) -> typing.List[types.Post]:
        """
        Retrieves posts from the user's timeline

        **Parameters:**

        - **page** (`int`, optional): Page number, defaults to 1

        **Returns:** [`types.Post[]`](/types/#post)

        **Authentication Required:** Yes
        """

        resp = (
            await self._sv.make_request(
                Request(
                    "timeline.retrieve_feed",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        ),
                        "page": page,
                    },
                )
            )
        ).unwrap()
        return [types.Post.from_json(i) for i in resp]

    @async_auto_create_session
    async def get_likers(
        self, post: typing.Union[str, types.Post], page: int = 1
    ) -> typing.List[types.Peer]:
        """
        Get the peers who liked a post

        **Parameters:**

        - **post** (`str`, [`types.Post`](/types/#post)): The post
        - **page** (`int`, optional): Page number, defaults to 1

        **Returns:** [`types.Peer[]`](/types/#peer)

        **Authentication Required:** Yes
        """

        if isinstance(post, types.Post):
            post = post.id
        resp = (
            await self._sv.make_request(
                Request(
                    "timeline.get_likes",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        ),
                        "post": post,
                        "page": page,
                    },
                )
            )
        ).unwrap()
        return [types.Peer.from_json(i) for i in resp]

    @async_auto_create_session
    async def get_reposters(
        self, post: typing.Union[str, types.Post], page: int = 1
    ) -> typing.List[types.Peer]:
        """
        Get the peers who reposted a post

        **Parameters:**

        - **post** (`str`, [`types.Post`](/types/#post)): The post
        - **page** (`int`, optional): Page number, defaults to 1

        **Returns:** [`types.Peer[]`](/types/#peer)

        **Authentication Required:** Yes
        """

        if isinstance(post, types.Post):
            post = post.id
        resp = (
            await self._sv.make_request(
                Request(
                    "timeline.get_reposted_peers",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        ),
                        "post": post,
                        "page": page,
                    },
                )
            )
        ).unwrap()
        return [types.Peer.from_json(i) for i in resp]

    @async_auto_create_session
    async def get_quotes(
        self, post: typing.Union[str, types.Post], page: int = 1
    ) -> typing.List[types.Post]:
        """
        Get posts that quoted the provided post

        **Parameters:**

        - **post** (`str`, [`types.Post`](/types/#post)): The post
        - **page** (`int`, optional): Page number, defaults to 1

        **Returns:** [`types.Peer[]`](/types/#peer)

        **Authentication Required:** Yes
        """

        if isinstance(post, types.Post):
            post = post.id
        resp = (
            await self._sv.make_request(
                Request(
                    "timeline.get_quotes",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        ),
                        "post": post,
                        "page": page,
                    },
                )
            )
        ).unwrap()
        return [types.Post.from_json(i) for i in resp]

    @async_auto_create_session
    async def get_replies(
        self, post: typing.Union[str, types.Post], page: int = 1
    ) -> typing.List[types.Post]:
        """
        Get posts that replied to the provided post

        **Parameters:**

        - **post** (`str`, [`types.Post`](/types/#post)): The post
        - **page** (`int`, optional): Page number, defaults to 1

        **Returns:** [`types.Peer[]`](/types/#peer)

        **Authentication Required:** Yes
        """

        if isinstance(post, types.Post):
            post = post.id
        resp = (
            await self._sv.make_request(
                Request(
                    "timeline.get_replies",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        ),
                        "post": post,
                        "page": page,
                    },
                )
            )
        ).unwrap()
        return [types.Post.from_json(i) for i in resp]

    async def iter_feed(
        self,
        start_page: int = 1,
    ) -> typing.Iterator[types.Post]:
        """
        Helper method to iterate through all the posts in the user's timeline

        - **start_page** (`int`, optional): Page to start off at, defaults to 1

        **Yields:** [`types.Post`](/types/#post)

        **Authentication Required:** Yes
        """

        server_info = await self._sv._get_cached_server_info()
        page = start_page
        while True:
            posts = await self.get_feed(page)
            for i in posts:
                yield i
            if not posts or len(posts) < server_info.retrieve_feed_max_limit:
                break
            page += 1

    async def iter_likers(
        self,
        post: typing.Union[str, types.Post],
        start_page: int = 1,
    ) -> typing.Iterator[types.Peer]:
        """
        Helper method to iterate through all the peers that liked the provided post

        - **post** (`str`, [`types.Post`](/types/#post)): The post
        - **start_page** (`int`, optional): Page to start off at, defaults to 1

        **Yields:** [`types.Peer`](/types/#peer)

        **Authentication Required:** Yes
        """

        server_info = await self._sv._get_cached_server_info()
        page = start_page
        while True:
            peers = await self.get_likers(post, page)
            for i in peers:
                yield i
            if not peers or len(peers) < server_info.retrieve_likes_max_limit:
                break
            page += 1

    async def iter_reposters(
        self,
        post: typing.Union[str, types.Post],
        start_page: int = 1,
    ) -> typing.Iterator[types.Peer]:
        """
        Helper method to iterate through all the peers that reposted the provided post

        - **post** (`str`, [`types.Post`](/types/#post)): The post
        - **start_page** (`int`, optional): Page to start off at, defaults to 1

        **Yields:** [`types.Peer`](/types/#peer)

        **Authentication Required:** Yes
        """

        server_info = await self._sv._get_cached_server_info()
        page = start_page
        while True:
            peers = await self.get_reposters(post, page)
            for i in peers:
                yield i
            if not peers or len(peers) < server_info.retrieve_reposts_max_limit:
                break
            page += 1

    async def iter_quotes(
        self,
        post: typing.Union[str, types.Post],
        start_page: int = 1,
    ) -> typing.Iterator[types.Post]:
        """
        Helper method to iterate through all the posts that quoted the provided post

        - **post** (`str`, [`types.Post`](/types/#post)): The post
        - **start_page** (`int`, optional): Page to start off at, defaults to 1

        **Yields:** [`types.Post`](/types/#post)

        **Authentication Required:** Yes
        """

        server_info = await self._sv._get_cached_server_info()
        page = start_page
        while True:
            posts = await self.get_quotes(post, page)
            for i in posts:
                yield i
            if not posts or len(posts) < server_info.retrieve_quotes_max_limit:
                break
            page += 1

    async def iter_replies(
        self,
        post: typing.Union[str, types.Post],
        start_page: int = 1,
    ) -> typing.Iterator[types.Post]:
        """
        Helper method to iterate through all the posts that replied to the provided post

        - **post** (`str`, [`types.Post`](/types/#post)): The post
        - **start_page** (`int`, optional): Page to start off at, defaults to 1

        **Yields:** [`types.Post`](/types/#post)

        **Authentication Required:** Yes
        """

        server_info = await self._sv._get_cached_server_info()
        page = start_page
        while True:
            posts = await self.get_replies(post, page)
            for i in posts:
                yield i
            if not posts or len(posts) < server_info.retrieve_replies_max_limit:
                break
            page += 1
