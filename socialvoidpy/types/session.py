from datetime import datetime

class Session:
    def __init__(self, id, flags, authenticated, created, expires):
        self.id = id
        self.flags = flags
        self.authenticated = authenticated
        self.created = datetime.fromtimestamp(created)
        self.expires = datetime.fromtimestamp(expires)
