import typing
from .. import types
from ..utils import create_session_id
from ..request import Request

if typing.TYPE_CHECKING:
    from . import SocialvoidClient


class Network:
    def __init__(self, sv: "SocialvoidClient"):
        self._sv = sv

    def get_me(self) -> types.Peer:
        return types.Peer.from_json(
            self._sv.make_request(
                Request(
                    "network.get_me",
                    {"session_identification": create_session_id(self._sv.session)},
                )
            ).unwrap()
        )