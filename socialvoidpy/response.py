import typing
from .errors import ERROR_MAP, GeneralError, JSONRPCError

class Response:
    def __init__(self, body: dict):
        self.id: str = body['id']
        self.success: bool = 'error' not in body
        self.data: typing.Optional[typing.Union[dict, list]] = body.get('result')
        self.error: typing.Optional[dict] = body.get('error')
        self.raw = body

    # Maybe a different name?
    def unwrap(self) -> typing.Union[dict, list]:
        if self.success:
            return self.data
        if self.error['code'] in ERROR_MAP:
            raise ERROR_MAP[self.error['code']](self.error['code'], self.error['message'], self.error.get('params'))
        if self.error['code'] >= -32768 and self.error['code'] <= -32000:
            raise JSONRPCError(self.error['code'], self.error['message'], self.error.get('params'))
        raise GeneralError(self.error['code'], self.error['message'], self.error.get('params'))
