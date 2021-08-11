import secrets
import requests
from ..utils import parse_jsonrpc_response, serialize_request
from .session import Session

class SocialvoidClient:
    # TODO Change endpoint parameter to an actual instance
    def __init__(self, filename=None, endpoint='http://127.0.0.1:6800/jsonrpc', http_session=None):
        self.endpoint = endpoint
        if http_session is None:
            http_session = requests.Session()
        self.http_session = http_session
        if filename is None:
            self.session = Session(self)
        else:
            self.session = Session.load(self, filename)
        self._session_filename = filename

    def _save_session(self):
        if self._session_filename is not None:
            self.session.save(self._session_filename)

    def make_request(self, *requests):
        if not requests:
            raise ValueError('requests should not be empty')
        batch = len(requests) != 1
        if not batch:
            requests = requests[0]
        body = serialize_request(requests)
        resp = self.http_session.post(self.endpoint, json=body)
        return parse_jsonrpc_response(resp.text, batch)
