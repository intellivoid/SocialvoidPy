import json
import secrets
from .. import types
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

    @classmethod
    def load(cls, sv, filename):
        with open(filename) as file:
            data = json.load(file)
        return cls(sv, data.get('public_hash'), data.get('private_hash'), data.get('session_id'), data.get('session_challenge'), data.get('session_exists'))

    def save(self, filename):
        with open(filename, 'w+') as file:
            json.dump({'public_hash': self.public_hash, 'private_hash': self.private_hash, 'session_id': self.session_id, 'session_challenge': self.session_challenge, 'session_exists': self.session_exists}, file)

    async def create(self, name='SocialvoidPy', version=version, platform=None):
        if platform is None:
            platform = get_platform()
        self.public_hash = public_hash = secrets.token_hex(32)
        self.private_hash = private_hash = secrets.token_hex(32)
        resp = (await self._sv.make_request(Request('session.create', {'public_hash': public_hash, 'private_hash': private_hash, 'name': name, 'version': version, 'platform': platform}))).unwrap()
        self.session_id = resp['id']
        self.session_challenge = resp['challenge']
        self.session_exists = True
        self._sv._save_session()

    async def get(self):
        return types.Session.from_json((await self._sv.make_request(Request('session.get', {'session_identification': create_session_id(self)}))).unwrap())

    async def logout(self):
        return (await self._sv.make_request(Request('session.logout', {'session_identification': create_session_id(self)}))).unwrap()

    async def authenticate_user(self, username, password, otp=None):
        params = {'session_identification': create_session_id(self), 'username': username, 'password': password}
        if otp is not None:
            params['otp'] = otp
        return (await self._sv.make_request(Request('session.authenticate_user', params))).unwrap()

    async def register(self, terms_of_service_id, username, password, first_name, last_name=None):
        params = {'session_identification': create_session_id(self), 'terms_of_service_id': terms_of_service_id, 'terms_of_service_agree': True, 'username': username, 'password': password, 'first_name': first_name, 'last_name': last_name}
        return types.Peer.from_json((await self._sv.make_request(Request('session.register', params))).unwrap())
