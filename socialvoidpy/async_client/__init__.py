import secrets
import pathlib
import typing
import httpx
from ..request import Request
from .. import types
from ..response import Response
from ..utils import (
    parse_jsonrpc_response,
    serialize_request,
    create_session_id,
    get_platform,
    maybe_await,
)
from ..version import version
from ..sync_sessionstorage import (
    AbstractSessionStorage,
    MemorySessionStorage,
    FileSessionStorage,
)
from ..async_sessionstorage import AsyncAbstractSessionStorage
from .session import Session
from .help import Help
from .network import Network
from .account import Account
from .cloud import Cloud
from .cdn import CDN


class AsyncSocialvoidClient:
    """
    Asynchronous Socialvoid client

    **Usage:**

    ```python
    >>> sv = socialvoidpy.AsyncSocialvoidClient("socialvoid.session")
    ```

    **Parameters:**

    - **session_storage** (`str`, `pathlib.Path`, `AbstractSessionStorage`, `AsyncAbstractSessionStorage`, `None`, optional): Path or session storage object for session data persistence
    - **rpc_endpoint** (`str`, optional): RPC endpoint url, set to the official instance by default
    - **auto_handle_sessions** (`bool`, optional): Automatically handle sessions, set to True by default
    - **client_name** (`str`, optional): The name of the client, defaults to SocialvoidPy
    - **client_version** (`str`, optional): The version of the client, defaults to socialvoidpy's version
    - **client_platform** (`str`, `None`, optional): The platform of the client, defaults to `platform.platform() or "Unknown"`
    """

    def __init__(
        self,
        session_storage: typing.Optional[
            typing.Union[
                str, pathlib.Path, AbstractSessionStorage, AsyncAbstractSessionStorage
            ]
        ] = None,
        rpc_endpoint: str = "http://socialvoid.qlg1.com:5601/",
        auto_handle_sessions: bool = True,
        client_name: str = "SocialvoidPy",
        client_version: str = version,
        client_platform: typing.Optional[str] = None,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        self.rpc_endpoint = rpc_endpoint
        if httpx_client is None:
            httpx_client = httpx.AsyncClient()
        self.httpx_client = httpx_client
        if session_storage is None:
            session_storage = MemorySessionStorage()
        elif isinstance(session_storage, (str, pathlib.Path)):
            session_storage = FileSessionStorage(session_storage)
        self.session_storage = session_storage
        self.auto_handle_sessions = auto_handle_sessions
        self.client_name = client_name
        self.client_version = client_version
        self.client_platform = client_platform or get_platform()
        self._cached_server_info = None
        self.session = Session(self)
        self.help = Help(self)
        self.network = Network(self)
        self.account = Account(self)
        self.cloud = Cloud(self)
        self.cdn = CDN(self)

    async def close(self):
        """
        Closes the session storage and httpx client, should be called after you're finished using the object
        """
        await maybe_await(self.session_storage.close())
        await self.httpx_client.aclose()

    async def _get_cached_server_info(self) -> types.ServerInformation:
        if not self._cached_server_info:
            self._cached_server_info = await self.help.get_server_information()
        return self._cached_server_info

    async def make_request(
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
        resp = await self.httpx_client.post(self.rpc_endpoint, json=body)
        return parse_jsonrpc_response(resp.text, batch)

    async def get_protocol_version(self) -> typing.Tuple[int]:
        """
        Returns the protocol version the server supports

        **Usage:**

        ```python
        >>> await sv.get_protocol_version()
        (1, 0)
        >>> await sv.get_protocol_version() >= (1, 1)
        False
        ```
        """

        return tuple(
            int(i)
            for i in (await self._get_cached_server_info()).protocol_version.split(".")
        )
