import typing
from .. import types
from ..utils import create_session_id, auto_create_session
from ..request import Request

if typing.TYPE_CHECKING:
    from . import SocialvoidClient


class Network:
    """
    `network` methods
    """

    def __init__(self, sv: "SocialvoidClient"):
        self._sv = sv

    @auto_create_session
    def get_me(self) -> types.Peer:
        """
        Gets the peer of the currently logged in account

        **Returns:** [`types.Peer`](/types/#peer)

        **Authentication Required:** Yes
        """

        return types.Peer.from_json(
            self._sv.make_request(
                Request(
                    "network.get_me",
                    {
                        "session_identification": create_session_id(
                            self._sv.session_storage
                        )
                    },
                )
            ).unwrap()
        )

    @auto_create_session
    def get_peer(self, peer: typing.Union[types.Peer, str]) -> types.Peer:
        """
        Get a peer (if you want yourself see `network.get_me`)

        **Parameters:**

        - **peer** ([`types.Peer`](/types/#peer), `str`): The peer ID or username (with leading @)

        **Returns:** [`types.Peer`](/types/#peer)

        **Authentication Required:** Yes
        """

        if isinstance(peer, types.Peer):
            peer = peer.id
        resp = self._sv.make_request(
            Request(
                "network.resolve_peer",
                {
                    "session_identification": create_session_id(
                        self._sv.session_storage
                    ),
                    "peer": peer,
                },
            )
        ).unwrap()
        return types.Peer.from_json(resp)

    @auto_create_session
    def get_profile(
        self, peer: typing.Optional[typing.Union[types.Peer, str]] = None
    ) -> types.Profile:
        """
        Get a peer's profile

        **Parameters:**

        - **peer** ([`types.Peer`](/types/#peer), `str`, `None`, optional): The peer ID or username (with leading @), defaults to the currently authenticated user if not specified

        **Returns:** [`types.Profile`](/types/#profile)

        **Authentication Required:** Yes
        """

        if isinstance(peer, types.Peer):
            peer = peer.id
        params = {"session_identification": create_session_id(self._sv.session_storage)}
        if peer:
            params["peer"] = peer
        resp = self._sv.make_request(Request("network.get_profile", params)).unwrap()
        return types.Profile.from_json(resp)

    @auto_create_session
    def follow_peer(
        self, peer: typing.Union[types.Peer, str]
    ) -> types.RelationshipType:
        """
        Follows the peer provided

        **Parameters:**

        - **peer** ([`types.Peer`](/types/#peer), `str`): The peer ID or username (with leading @) to follow

        **Returns:** [`types.RelationshipType`](/types/#relationshiptype)

        **Authentication Required:** Yes
        """

        if isinstance(peer, types.Peer):
            peer = peer.id
        resp = self._sv.make_request(
            Request(
                "network.follow_peer",
                {
                    "session_identification": create_session_id(
                        self._sv.session_storage
                    ),
                    "peer": peer,
                },
            )
        ).unwrap()
        return types.RelationshipType(resp)

    @auto_create_session
    def unfollow_peer(
        self, peer: typing.Union[types.Peer, str]
    ) -> types.RelationshipType:
        """
        Unfollows the peer provided

        **Parameters:**

        - **peer** ([`types.Peer`](/types/#peer), `str`): The peer ID or username (with leading @) to follow

        **Returns:** [`types.RelationshipType`](/types/#relationshiptype)

        **Authentication Required:** Yes
        """

        if isinstance(peer, types.Peer):
            peer = peer.id
        resp = self._sv.make_request(
            Request(
                "network.unfollow_peer",
                {
                    "session_identification": create_session_id(
                        self._sv.session_storage
                    ),
                    "peer": peer,
                },
            )
        ).unwrap()
        return types.RelationshipType(resp)

    @auto_create_session
    def get_followers(
        self, peer: typing.Optional[typing.Union[types.Peer, str]] = None, page: int = 1
    ) -> typing.List[types.Peer]:
        """
        Get a peer's followers

        **Parameters:**

        - **peer** ([`types.Peer`](/types/#peer), `str`, `None`, optional): The peer ID or username (with leading @), defaults to the currently authenticated user if not specified
        - **page** (`int`, optional): Page number, defaults to 1

        **Returns:** [`types.Peer[]`](/types/#peer)

        **Authentication Required:** Yes
        """

        if isinstance(peer, types.Peer):
            peer = peer.id
        params = {
            "session_identification": create_session_id(self._sv.session_storage),
            "page": page,
        }
        if peer:
            params["peer"] = peer
        resp = self._sv.make_request(Request("network.get_followers", params)).unwrap()
        return [types.Peer.from_json(i) for i in resp]

    @auto_create_session
    def get_following(
        self, peer: typing.Optional[typing.Union[types.Peer, str]] = None, page: int = 1
    ) -> typing.List[types.Peer]:
        """
        Get what peers the provided peer follows

        **Parameters:**

        - **peer** ([`types.Peer`](/types/#peer), `str`, `None`, optional): The peer ID or username (with leading @), defaults to the currently authenticated user if not specified
        - **page** (`int`, optional): Page number, defaults to 1

        **Returns:** [`types.Peer[]`](/types/#peer)

        **Authentication Required:** Yes
        """

        if isinstance(peer, types.Peer):
            peer = peer.id
        params = {
            "session_identification": create_session_id(self._sv.session_storage),
            "page": page,
        }
        if peer:
            params["peer"] = peer
        resp = self._sv.make_request(Request("network.get_following", params)).unwrap()
        return [types.Peer.from_json(i) for i in resp]

    def iter_followers(
        self,
        peer: typing.Optional[typing.Union[types.Peer, str]] = None,
        start_page: int = 1,
    ) -> typing.Iterator[types.Peer]:
        """
        Helper method to iterate through all of a peer's followers

        - **peer** ([`types.Peer`](/types/#peer), `str`, `None`, optional): The peer ID or username (with leading @), defaults to the currently authenticated user if not specified
        - **start_page** (`int`, optional): Page to start off at, defaults to 1

        **Yields:** [`types.Peer`](/types/#peer)

        **Authentication Required:** Yes
        """

        server_info = self._sv.help.get_server_information()
        page = start_page
        while True:
            peers = self.get_followers(peer, page)
            yield from peers
            if not peers or len(peers) < server_info.retrieve_followers_max_limit:
                break
            page += 1

    def iter_following(
        self,
        peer: typing.Optional[typing.Union[types.Peer, str]] = None,
        start_page: int = 1,
    ) -> typing.Iterator[types.Peer]:
        """
        Helper method to iterate through all peers that a peer follows

        - **peer** ([`types.Peer`](/types/#peer), `str`, `None`, optional): The peer ID or username (with leading @), defaults to the currently authenticated user if not specified
        - **start_page** (`int`, optional): Page to start off at, defaults to 1

        **Yields:** [`types.Peer`](/types/#peer)

        **Authentication Required:** Yes
        """

        server_info = self._sv.help.get_server_information()
        page = start_page
        while True:
            peers = self.get_following(peer, page)
            yield from peers
            if not peers or len(peers) < server_info.retrieve_following_max_limit:
                break
            page += 1
