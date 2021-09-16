from .. import types
from ..utils import create_session_id
from ..request import Request

class Network:
    def __init__(self, sv):
        self._sv = sv

    def get_me(self):
        return types.Peer.from_json(self._sv.make_request(Request('network.get_me', {'session_identification': create_session_id(self._sv.session)})).unwrap())
