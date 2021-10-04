import json
import typing
import platform
from .request import Request
from .response import Response
from .session_challenge import answer_challenge
from .types.text_entity import TEXT_ENTITY_MAP, _TextEntity
from .errors import SessionDoesNotExist


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


def create_session_id(session) -> dict:
    if not session.session_exists:
        raise SessionDoesNotExist(None, "Session does not exist", None)
    return {
        "session_id": session.session_id,
        "client_public_hash": session.public_hash,
        "challenge_answer": answer_challenge(
            session.private_hash, session.session_challenge
        ),
    }


def raw_textentities_to_types(entities) -> typing.List[_TextEntity]:
    return [TEXT_ENTITY_MAP.get(i["type"], _TextEntity).from_json(i) for i in entities]
