from .errors import ERROR_MAP, GeneralError, JSONRPCError

class Response:
    def __init__(self, body):
        self.id = body['id']
        self.success = 'error' not in body
        self.data = body.get('result')
        self.error = body.get('error')
        self.raw = body

    # Maybe a different name?
    def unwrap(self):
        if self.success:
            return self.data
        if self.error['code'] in ERROR_MAP:
            raise ERROR_MAP[self.error['code']](self.error['code'], self.error['message'], self.error.get('params'))
        if self.error['code'] >= -32768 and self.error['code'] <= -32000:
            raise JSONRPCError(self.error['code'], self.error['message'], self.error.get('params'))
        raise GeneralError(self.error['code'], self.error['message'], self.error.get('params'))
