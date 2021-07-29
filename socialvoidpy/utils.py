import json
from .request import Request
from .response import Response

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
