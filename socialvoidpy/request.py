import time
import typing


class Request:
    def __init__(
        self,
        method: str,
        params: typing.Optional[
            typing.Union[typing.Dict[str, typing.Any], list]
        ] = None,
        notification: bool = False,
    ):
        self.method = method
        self.params = params
        self.id: typing.Optional[str] = (
            str(time.monotonic()) if not notification else None
        )
