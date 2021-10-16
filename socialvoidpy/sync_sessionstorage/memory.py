import typing
from .abstract import AbstractSessionStorage


class MemorySessionStorage(AbstractSessionStorage):
    def __init__(self):
        self._public_hash = None
        self._private_hash = None
        self._session_id = None
        self._session_challenge = None

    def get_public_hash(self) -> typing.Optional[str]:
        return self._public_hash

    def get_private_hash(self) -> typing.Optional[str]:
        return self._private_hash

    def get_session_id(self) -> typing.Optional[str]:
        return self._session_id

    def get_session_challenge(self) -> typing.Optional[str]:
        return self._session_challenge

    def set_public_hash(self, public_hash: str):
        self._public_hash = public_hash

    def set_private_hash(self, private_hash: str):
        self._private_hash = private_hash

    def set_session_id(self, session_id: str):
        self._session_id = session_id

    def set_session_challenge(self, session_challenge: str):
        self._session_challenge = session_challenge

    def close(self):
        pass

    def flush(self):
        pass
