import secrets
import requests
from . import types
from .request import Request
from .utils import parse_jsonrpc_response, serialize_request, get_platform, create_session_id
from .session import Session
from .version import version

class SocialvoidClient:
    # TODO Change endpoint parameter to an actual instance
    def __init__(self, filename=None, endpoint='http://127.0.0.1:6800/jsonrpc', http_session=None):
        self.endpoint = endpoint
        if http_session is None:
            http_session = requests.Session()
        self.http_session = http_session
        if filename is None:
            self.session = Session()
        else:
            self.session = Session.load(filename)
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

    def create_session(self, name='SocialvoidPy', version=version, platform=None):
        if platform is None:
            platform = get_platform()
        self.session.public_hash = public_hash = secrets.token_hex(64)
        self.session.private_hash = private_hash = secrets.token_hex(64)
        resp = self.make_request(Request('session.create', {'public_hash': public_hash, 'private_hash': private_hash, 'name': name, 'version': version, 'platform': platform})).unwrap()
        self.session.session_id = resp['id']
        self.session.session_challenge = resp['challenge']
        self._save_session()

    def get_session(self):
        return types.Session(**self.make_request(Request('session.get', {'session_identification': create_session_id(self.session)})).unwrap())

    def logout(self):
        return self.make_request(Request('session.logout', {'session_identification': create_session_id(self.session)})).unwrap()
