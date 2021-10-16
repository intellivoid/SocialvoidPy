import json
import typing
import pathlib
from .memory import MemorySessionStorage


class FileSessionStorage(MemorySessionStorage):
    def __init__(self, file: typing.Union[str, pathlib.Path]):
        super().__init__()
        self._file = file
        try:
            with open(file) as file:
                data = json.load(file)
        except FileNotFoundError:
            return
        if data.get("public_hash"):
            self.set_public_hash(data["public_hash"])
        if data.get("private_hash"):
            self.set_private_hash(data["private_hash"])
        if data.get("session_id"):
            self.set_session_id(data["session_id"])
        if data.get("session_challenge"):
            self.set_session_challenge(data["session_challenge"])

    def flush(self):
        public_hash = self.get_public_hash()
        private_hash = self.get_private_hash()
        session_id = self.get_session_id()
        session_challenge = self.get_session_challenge()
        # Backwards compatibility, should it be removed?
        session_exists = (
            public_hash and private_hash and session_id and session_challenge
        )
        with open(self._file, "w") as file:
            json.dump(
                {
                    "public_hash": public_hash,
                    "private_hash": private_hash,
                    "session_id": session_id,
                    "session_challenge": session_challenge,
                    "session_exists": session_exists,
                },
                file,
            )
