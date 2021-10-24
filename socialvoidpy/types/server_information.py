from dataclasses import dataclass
from .base_class import BaseClass


@dataclass
class ServerInformation(BaseClass):
    """
    Information about the server

    **Members:**

    - **network_name** (`str`): The name of the network
    - **protocol_version** (`str`): The version of the protocol standard being used
    - **cdn_server** (`str`): URL to the CDN server
    - **upload_max_file_size** (`int`): Maximum upload file size in bytes
    - **unauthorized_session_ttl** (`int`): How long an unauthorized session can be unused before it expires
    - **authorized_session_ttl** (`int`): How long an authorized session can be unused before it expires
    - **retrieve_likes_max_limit** (`int`): The maximum amount of likes that can be retrieved at once with `timeline.get_likes` via the `page` parameter
    - **retrieve_reposts_max_limit** (`int`): The maximum amount of reposts that can be retrieved at once with `timeline.get_reposted_peers` via the `page` parameter
    - **retrieve_replies_max_limit** (`int`): The maximum amount of replies that can be retrieved at once with `timeline.get_replies` via the `page` parameter
    - **retrieve_quotes_max_limit** (`int`): The maximum amount of quotes that can be retrieved at once with `timeline.get_quotes` via the `page` parameter
    - **retrieve_feed_max_limit** (`int`): The maximum amount of posts that can be retrieved at once with `timeline.get_feed` via the `page` parameter
    - **retrieve_followers_max_limit** (`int`): The maximum amount of followers that can be retrieved at once with `network.get_followers` via the `page` parameter
    - **retrieve_following_max_limit** (`int`): The maximum amount of following peers that can be retrieved at once with `network.get_following` via the `page` parameter
    """

    network_name: str
    protocol_version: str
    cdn_server: str
    upload_max_file_size: int
    unauthorized_session_ttl: int
    authorized_session_ttl: int
    retrieve_likes_max_limit: int
    retrieve_reposts_max_limit: int
    retrieve_replies_max_limit: int
    retrieve_quotes_max_limit: int
    retrieve_feed_max_limit: int
    retrieve_followers_max_limit: int
    retrieve_following_max_limit: int

    @classmethod
    def from_json(cls, resp: dict):
        return cls(
            resp["network_name"],
            resp["protocol_version"],
            resp["cdn_server"],
            resp["upload_max_file_size"],
            resp["unauthorized_session_ttl"],
            resp["authorized_session_ttl"],
            resp["retrieve_likes_max_limit"],
            resp["retrieve_reposts_max_limit"],
            resp["retrieve_replies_max_limit"],
            resp["retrieve_quotes_max_limit"],
            resp["retrieve_feed_max_limit"],
            resp["retrieve_followers_max_limit"],
            resp["retrieve_following_max_limit"],
        )
