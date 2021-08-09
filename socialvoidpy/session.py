import json

class Session:
    def __init__(self, public_hash=None, private_hash=None, session_id=None, session_challenge=None):
        self.public_hash = public_hash
        self.private_hash = private_hash
        self.session_id = session_id
        self.session_challenge = session_challenge

    @classmethod
    def load(cls, filename):
        with open(filename) as file:
            data = json.load(file)
        return cls(**data)

    def save(self, filename):
        with open(filename, 'w+') as file:
            json.dump({'public_hash': self.public_hash, 'private_hash': self.private_hash, 'session_id': self.session_id, 'session_challenge': self.session_challenge}, file)
