import requests
from .utils import parse_jsonrpc_response, serialize_request

class SocialvoidClient:
    # TODO Change endpoint parameter to an actual instance
    def __init__(self, endpoint='http://127.0.0.1:6800/jsonrpc', session=None):
        self.endpoint = endpoint
        if session is None:
            session = requests.Session()
        self.session = session

    def make_request(self, *requests):
        if not requests:
            raise ValueError('requests should not be empty')
        batch = len(requests) != 1
        if not batch:
            requests = requests[0]
        body = serialize_request(requests)
        resp = self.session.post(self.endpoint, json=body)
        return parse_jsonrpc_response(resp.text, batch)
