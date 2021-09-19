import typing


class GeneralError(Exception):
    def __init__(
        self,
        code: typing.Optional[int],
        message: str,
        data: typing.Optional[typing.Union[dict, list]],
    ):
        super().__init__(message)
        self.code = code
        self.data = data


# Can this go somewhere else?
class SessionDoesNotExist(GeneralError):
    pass
