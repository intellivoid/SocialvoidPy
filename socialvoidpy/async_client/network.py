import typing
from .. import types
from ..utils import async_create_session_id, async_auto_create_session
from ..request import Request

if typing.TYPE_CHECKING:
    from . import AsyncSocialvoidClient


class Network:
    """
    `network` methods
    """

    def __init__(self, sv: "AsyncSocialvoidClient"):
        self._sv = sv

    @async_auto_create_session
    async def get_me(self) -> types.Peer:
        """
        Gets the peer of the currently logged in account

        **Returns:** [`types.Peer`](/types/#peer)

        **Authentication Required:** Yes
        """

        return types.Peer.from_json(
            (
                await self._sv.make_request(
                    Request(
                        "network.get_me",
                        {
                            "session_identification": await async_create_session_id(
                                self._sv.session_storage
                            )
                        },
                    )
                )
            ).unwrap()
        )
