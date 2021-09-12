import json
import secrets
from .. import types
from ..errors import SessionDoesNotExist
from ..request import Request
from ..utils import get_platform, create_session_id
from ..version import version

class Session:
    def __init__(self, sv, public_hash=None, private_hash=None, session_id=None, session_challenge=None, session_exists=False):
        self._sv = sv
        self.public_hash = public_hash
        self.private_hash = private_hash
        self.session_id = session_id
        self.session_challenge = session_challenge
        self.session_exists = session_exists

    def _assert_existence(self):
        if not self.session_exists:
            raise SessionDoesNotExist(None, 'Session does not exist', None)

    @classmethod
    def load(cls, sv, filename):
        with open(filename) as file:
            data = json.load(file)
        return cls(sv, **data)

    def save(self, filename):
        with open(filename, 'w+') as file:
            json.dump({'public_hash': self.public_hash, 'private_hash': self.private_hash, 'session_id': self.session_id, 'session_challenge': self.session_challenge, 'session_exists': self.session_exists}, file)

    def create(self, name='SocialvoidPy', version=version, platform=None):
        if platform is None:
            platform = get_platform()
        self.public_hash = public_hash = secrets.token_hex(32)
        self.private_hash = private_hash = secrets.token_hex(32)
        resp = self._sv.make_request(Request('session.create', {'public_hash': public_hash, 'private_hash': private_hash, 'name': name, 'version': version, 'platform': platform})).unwrap()
        self.session_id = resp['id']
        self.session_challenge = resp['challenge']
        self.session_exists = True
        self._sv._save_session()

    def get(self):
        self._assert_existence()
        return types.Session.from_json(self._sv.make_request(Request('session.get', {'session_identification': create_session_id(self)})).unwrap())

    def logout(self):
        self._assert_existence()
        return self._sv.make_request(Request('session.logout', {'session_identification': create_session_id(self)})).unwrap()

    def authenticate_user(self, username, password, otp=None):
        self._assert_existence()
        params = {'session_identification': create_session_id(self), 'username': username, 'password': password}
        if otp is not None:
            params['otp'] = otp
        return self._sv.make_request(Request('session.authenticate_user', params)).unwrap()
