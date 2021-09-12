import secrets
import requests
from ..utils import parse_jsonrpc_response, serialize_request
from .session import Session
from .help import Help
from .network import Network

class SocialvoidClient:
    def __init__(self, filename=None, rpc_endpoint='http://socialvoid.qlg1.com:5601/', http_session=None):
        self.rpc_endpoint = rpc_endpoint
        if http_session is None:
            http_session = requests.Session()
        self.http_session = http_session
        if filename is None:
            self.session = Session(self)
        else:
            try:
                self.session = Session.load(self, filename)
            except FileNotFoundError:
                self.session = Session(self)
        self._session_filename = filename
        self.help = Help(self)
        self.network = Network(self)

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
        resp = self.http_session.post(self.rpc_endpoint, json=body)
        return parse_jsonrpc_response(resp.text, batch)
