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
