import json
import platform
from .request import Request
from .response import Response
from .session_challenge import answer_challenge

def parse_jsonrpc_response(body, batch):
    if not body:
        if batch:
            return []
        return None
    body = json.loads(body)
    if isinstance(body, list):
        return list(map(Response, filter(lambda i: 'id' in i, body)))
    if 'id' in body:
        return Response(body)
    return None

def serialize_request(request):
    if hasattr(request, '__iter__'):
        return list(map(serialize_request, request))
    body = {'jsonrpc': '2.0', 'method': request.method}
    if request.id is not None:
        body['id'] = request.id
    if request.params is not None:
        body['params'] = request.params
    return body

def get_platform():
    return platform.system() or 'Unknown'

def create_session_id(session):
    return {'session_id': session.session_id, 'client_public_hash': session.public_hash, 'challenge_answer': answer_challenge(session.private_hash, session.session_challenge)}
