from dataclasses import dataclass
from .base_class import BaseClass

@dataclass
class ServerInformation(BaseClass):
    network_name: str
    protocol_version: str
    cdn_server: str
    upload_max_file_size: int
    unauthorized_session_ttl: int
    authorized_session_ttl: int

    @classmethod
    def from_json(cls, resp: dict):
        return cls(resp['network_name'], resp['protocol_version'], resp['cdn_server'], resp['upload_max_file_size'], resp['unauthorized_session_ttl'], resp['authorized_session_ttl'])
