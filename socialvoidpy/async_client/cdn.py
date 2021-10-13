import typing
import pathlib
from .. import types
from ..utils import create_session_id
from ..errors import ERROR_MAP, JSONRPCError, GeneralError

if typing.TYPE_CHECKING:
    from . import AsyncSocialvoidClient


class CDN:
    """
    `cdn` methods
    """

    def __init__(self, sv: "AsyncSocialvoidClient"):
        self._sv = sv

    async def stream(self, document: typing.Union[str, types.Document]):
        """
        Stream a document's contents

        **Parameters:**

        - **document**: Document to stream the contents of

        **Yields:** `bytes`

        **Authentication Required:** Yes (for now?)
        """

        if isinstance(document, types.Document):
            document = document.id
        params = {
            **create_session_id(self._sv.session),
            "action": "download",
            "document": document,
        }
        server_info = await self._sv._get_cached_server_info()
        async with self._sv.httpx_client.stream(
            "POST", server_info.cdn_server, data=params
        ) as resp:
            if resp.status_code != 200:
                await resp.read()
                error = await resp.json()
                if error["error_code"] in ERROR_MAP:
                    raise ERROR_MAP[error["error_code"]](
                        error["error_code"], error["message"], None
                    )
                if error["error_code"] >= -32768 and error["error_code"] <= -32000:
                    raise JSONRPCError(error["error_code"], error["message"], None)
                raise GeneralError(error["error_code"], error["message"], None)
            async for i in resp.iter_bytes():
                yield i

    async def upload(
        self, file: typing.Union[str, pathlib.Path, typing.BinaryIO]
    ) -> types.Document:
        """
        Upload a document

        **Parameters:**

        - **file**: File path or object to upload

        **Returns:** [`types.Document`](/types/#document)

        **Authentication Required:** Yes (for now?)
        """

        params = {
            **create_session_id(self._sv.session),
            "action": "upload",
        }
        server_info = await self._sv._get_cached_server_info()
        if isinstance(file, (str, pathlib.Path)):
            file = open(file, "rb")
        resp = await (
            await self._sv.httpx_client.post(
                server_info.cdn_server,
                data=params,
                files={"document": file},
            )
        ).json()
        if not resp["success"]:
            if resp["error_code"] in ERROR_MAP:
                raise ERROR_MAP[resp["error_code"]](
                    resp["error_code"], resp["message"], None
                )
            if resp["error_code"] >= -32768 and resp["error_code"] <= -32000:
                raise JSONRPCError(resp["error_code"], resp["message"], None)
            raise GeneralError(resp["error_code"], resp["message"], None)
        return types.Document.from_json(resp["results"])
