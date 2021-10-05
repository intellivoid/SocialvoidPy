import typing
from .. import types
from ..utils import create_session_id
from ..request import Request

if typing.TYPE_CHECKING:
    from . import AsyncSocialvoidClient


class Network:
    """
    `network` methods
    """

    def __init__(self, sv: "AsyncSocialvoidClient"):
        self._sv = sv

    async def get_me(self) -> types.Peer:
        """
        Gets the peer of the currently logged in account

        **Returns:** [`types.Peer`](/types/#peer)
        """

        return types.Peer.from_json(
            (
                await self._sv.make_request(
                    Request(
                        "network.get_me",
                        {"session_identification": create_session_id(self._sv.session)},
                    )
                )
            ).unwrap()
        )
