import secrets
import typing
import httpx
from ..response import Response
from ..utils import parse_jsonrpc_response, serialize_request
from .session import Session
from .help import Help
from .network import Network
from .account import Account
from .cloud import Cloud


class AsyncSocialvoidClient:
    def __init__(
        self,
        filename: typing.Optional[str] = None,
        rpc_endpoint: str = "http://socialvoid.qlg1.com:5601/",
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        self.rpc_endpoint = rpc_endpoint
        if httpx_client is None:
            httpx_client = httpx.AsyncClient()
        self.httpx_client = httpx_client
        if filename is None:
            self.session = Session(self)
        else:
            try:
                self.session = Session.load(self, filename)
            except FileNotFoundError:
                self.session = Session(self)
        self._session_filename = filename
        self.help = Help(self)
        self.network = Network(self)
        self.account = Account(self)
        self.cloud = Cloud(self)

    async def aclose(self):
        await self.httpx_client.aclose()

    def _save_session(self):
        if self._session_filename is not None:
            self.session.save(self._session_filename)

    async def make_request(self, *requests) -> typing.Union[list[Response], Response]:
        if not requests:
            raise ValueError("requests should not be empty")
        batch = len(requests) != 1
        if not batch:
            requests = requests[0]
        body = serialize_request(requests)
        resp = await self.httpx_client.post(self.rpc_endpoint, json=body)
        return parse_jsonrpc_response(resp.text, batch)
