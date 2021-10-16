import json
import typing
import inspect
import platform
import functools
from .request import Request
from .response import Response
from .sync_sessionstorage import AbstractSessionStorage
from .async_sessionstorage import AsyncAbstractSessionStorage
from .session_challenge import answer_challenge
from .types.text_entity import TEXT_ENTITY_MAP, _TextEntity
from .errors import SessionDoesNotExist, SessionNotFound, SessionExpired


def parse_jsonrpc_response(
    body: str, batch: bool
) -> typing.Optional[typing.Union[typing.List[Response], Response]]:
    if not body:
        if batch:
            return []
        return None
    body = json.loads(body)
    if isinstance(body, list):
        return list(map(Response, filter(lambda i: "id" in i, body)))
    if "id" in body:
        return Response(body)
    return None


def serialize_request(request: Request) -> typing.Union[typing.List[dict], dict]:
    if hasattr(request, "__iter__"):
        return list(map(serialize_request, request))
    body = {"jsonrpc": "2.0", "method": request.method}
    if request.id is not None:
        body["id"] = request.id
    if request.params is not None:
        body["params"] = request.params
    return body


def get_platform() -> str:
    return platform.system() or "Unknown"


_maybe_await_T = typing.TypeVar("T")


async def maybe_await(
    thing: typing.Union[_maybe_await_T, typing.Awaitable[_maybe_await_T]]
) -> _maybe_await_T:
    if inspect.isawaitable(thing):
        thing = await thing
    return thing


def create_session_id(session: AbstractSessionStorage) -> dict:
    public_hash = session.get_public_hash()
    private_hash = session.get_private_hash()
    session_id = session.get_session_id()
    session_challenge = session.get_session_challenge()
    session_exists = public_hash and private_hash and session_id and session_challenge
    if not session_exists:
        raise SessionDoesNotExist(None, "Session does not exist", None)
    return {
        "session_id": session_id,
        "client_public_hash": public_hash,
        "challenge_answer": answer_challenge(private_hash, session_challenge),
    }


async def async_create_session_id(
    session: typing.Union[AsyncAbstractSessionStorage, AbstractSessionStorage]
) -> dict:
    if isinstance(session, AbstractSessionStorage):
        return create_session_id(session)
    public_hash = await session.get_public_hash()
    private_hash = await session.get_private_hash()
    session_id = await session.get_session_id()
    session_challenge = await session.get_session_challenge()
    session_exists = public_hash and private_hash and session_id and session_challenge
    if not session_exists:
        raise SessionDoesNotExist(None, "Session does not exist", None)
    return {
        "session_id": session_id,
        "client_public_hash": public_hash,
        "challenge_answer": answer_challenge(private_hash, session_challenge),
    }


def raw_textentities_to_types(entities) -> typing.List[_TextEntity]:
    return [TEXT_ENTITY_MAP.get(i["type"], _TextEntity).from_json(i) for i in entities]


def auto_create_session(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kw):
        try:
            return func(self, *args, **kw)
        except (SessionDoesNotExist, SessionNotFound, SessionExpired):
            if not self._sv.auto_handle_sessions:
                raise
            self._sv.session.create()
            return func(self, *args, **kw)

    return wrapper


def async_auto_create_session(func):
    @functools.wraps(func)
    async def wrapper(self, *args, **kw):
        try:
            return await func(self, *args, **kw)
        except (SessionDoesNotExist, SessionNotFound, SessionExpired):
            if not self._sv.auto_handle_sessions:
                raise
            await self._sv.session.create()
            return await func(self, *args, **kw)

    return wrapper
