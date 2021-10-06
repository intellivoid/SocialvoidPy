import typing


class GeneralError(Exception):
    """
    The base exception for errors in the server's response
    """

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
    """
    Session does not exist while the method called requires a session
    """

    pass
