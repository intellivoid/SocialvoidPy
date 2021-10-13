import typing
import secrets
import httpx
from ..request import Request
from ..response import Response
from ..utils import parse_jsonrpc_response, serialize_request, create_session_id
from .. import types
from .session import Session
from .help import Help
from .network import Network
from .account import Account
from .cloud import Cloud
from .cdn import CDN


class SocialvoidClient:
    """
    Synchronous Socialvoid client

    **Usage:**

    ```python
    >>> sv = socialvoidpy.SocialvoidClient('socialvoid.session')
    ```

    **Parameters:**

    - **filename** *(optional)*: Path for session persistence
    - **rpc_endpoint** *(optional)*: RPC endpoint url, set to the official instance by defaul
    """

    def __init__(
        self,
        filename: typing.Optional[str] = None,
        rpc_endpoint: str = "http://socialvoid.qlg1.com:5601/",
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        self.rpc_endpoint = rpc_endpoint
        if httpx_client is None:
            httpx_client = httpx.Client()
        self.httpx_client = httpx_client
        if filename is None:
            self.session = Session(self)
        else:
            try:
                self.session = Session.load(self, filename)
            except FileNotFoundError:
                self.session = Session(self)
        self._session_filename = filename
        self._cached_server_info = None
        self.help = Help(self)
        self.network = Network(self)
        self.account = Account(self)
        self.cloud = Cloud(self)
        self.cdn = CDN(self)

    def close(self):
        """
        Closes the HTTPX client, should be called after you're finished using the object
        """
        self.httpx_client.close()

    def __del__(self):
        self.close()

    def _save_session(self):
        if self._session_filename is not None:
            self.session.save(self._session_filename)

    def _get_cached_server_info(self) -> types.ServerInformation:
        if not self._cached_server_info:
            self._cached_server_info = self.help.get_server_information()
        return self._cached_server_info

    def make_request(
        self, *requests: typing.Sequence[Request]
    ) -> typing.Union[typing.List[Response], Response]:
        """
        Sends request(s) off to RPC server, should not be used if a friendly method is available
        """
        if not requests:
            raise ValueError("requests should not be empty")
        batch = len(requests) != 1
        if not batch:
            requests = requests[0]
        body = serialize_request(requests)
        resp = self.httpx_client.post(self.rpc_endpoint, json=body)
        return parse_jsonrpc_response(resp.text, batch)

    def get_protocol_version(self) -> typing.Tuple[int]:
        """
        Returns the protocol version the server supports (the result is cached)

        **Usage:**

        ```python
        >>> sv.get_protocol_version()
        (1, 0)
        >>> sv.get_protocol_version() >= (1, 1)
        False
        ```

        **Session Required:** No
        """

        return tuple(
            int(i) for i in self._get_cached_server_info().protocol_version.split(".")
        )
