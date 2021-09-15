from ..utils import create_session_id
from ..request import Request

class Account:
    def __init__(self, sv):
        self._sv = sv

    def delete_profile_picture(self):
        self._sv.session.assert_existence()
        return self._sv.make_request(Request('account.delete_profile_picture', {'session_identification': create_session_id(self._sv.session)})).unwrap()

    def set_profile_picture(self, document_id):
        self._sv.session.assert_existence()
        return self._sv.make_request(Request('account.set_profile_picture', {'session_identification': create_session_id(self._sv.session), 'document': document_id})).unwrap()
