from dataclasses import dataclass
from .base_class import BaseClass


@dataclass
class ServerInformation(BaseClass):
    """
    Information about the server

    **Members:**

    - **network_name**: The name of the network
    - **protocol_version**: The version of the protocol standard being used
    - **cdn_server**: URL to the CDN server
    - **upload_max_file_size**: Maximum upload file size in bytes
    - **unauthorized_session_ttl**: How long an unauthorized session can be unused before it expires
    - **authorized_session_ttl**: How long an authorized session can be unused before it expires
    """

    network_name: str
    protocol_version: str
    cdn_server: str
    upload_max_file_size: int
    unauthorized_session_ttl: int
    authorized_session_ttl: int

    @classmethod
    def from_json(cls, resp: dict):
        return cls(
            resp["network_name"],
            resp["protocol_version"],
            resp["cdn_server"],
            resp["upload_max_file_size"],
            resp["unauthorized_session_ttl"],
            resp["authorized_session_ttl"],
        )
