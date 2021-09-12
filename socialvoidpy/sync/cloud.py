from .. import types
from ..utils import create_session_id
from ..request import Request

class Cloud:
    def __init__(self, sv):
        self._sv = sv

    def get_document(self, document_id):
        self._sv.session.assert_existence()
        return types.Document.from_json(self._sv.make_request(Request('cloud.get_document', {'session_identification': create_session_id(self._sv.session), 'document': document_id})).unwrap())
