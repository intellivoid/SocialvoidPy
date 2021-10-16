import sys
import typing
import configparser
from socialvoidpy import SocialvoidClient
from socialvoidpy.sync_sessionstorage import MemorySessionStorage


class INIWithSeperatedChallengeSessionStorage(MemorySessionStorage):
    def __init__(self, filename: str, session_challenge: typing.Optional[str]):
        super().__init__()
        self._config = configparser.ConfigParser()
        self._config.read(filename)
        self._filename = filename
        if session_challenge:
            self.set_public_hash(self._config["socialvoid"]["public_hash"])
            self.set_private_hash(self._config["socialvoid"]["private_hash"])
            self.set_session_id(self._config["socialvoid"]["session_id"])
            self.set_session_challenge(session_challenge)

    def flush(self):
        self._config["socialvoid"] = dict()
        self._config["socialvoid"]["public_hash"] = sv.session_storage.get_public_hash()
        self._config["socialvoid"][
            "private_hash"
        ] = sv.session_storage.get_private_hash()
        self._config["socialvoid"]["session_id"] = sv.session_storage.get_session_id()
        with open(self._filename, "w") as file:
            self._config.write(file)


# Could be safer but this is an example
try:
    session_challenge = sys.argv[1]
except IndexError:
    session_challenge = None
sv = SocialvoidClient(
    INIWithSeperatedChallengeSessionStorage("session.ini", session_challenge)
)
try:
    if session_challenge is None:
        sv.session.create("Fridgevoid", "1.0.1", "Samsung Smart Fridge")
        print(
            "Session challenge (keep it safe! use by passing as an argument):",
            sv.session_storage.get_session_challenge(),
        )
    else:
        print(sv.session.get())
finally:
    sv.close()
