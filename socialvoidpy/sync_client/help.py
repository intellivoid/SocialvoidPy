from .. import types
from ..request import Request

class Help:
    def __init__(self, sv):
        self._sv = sv

    def get_community_guidelines(self):
        resp = self._sv.make_request(Request('help.get_community_guidelines')).unwrap()
        return types.HelpDocument.from_json(resp)

    def get_privacy_policy(self):
        resp = self._sv.make_request(Request('help.get_privacy_policy')).unwrap()
        return types.HelpDocument.from_json(resp)

    def get_server_information(self):
        resp = self._sv.make_request(Request('help.get_server_information')).unwrap()
        return types.ServerInformation.from_json(resp)

    def get_terms_of_service(self):
        resp = self._sv.make_request(Request('help.get_terms_of_service')).unwrap()
        return types.HelpDocument.from_json(resp)
