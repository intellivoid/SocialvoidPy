from .general_error import GeneralError


class JSONRPCError(GeneralError):
    """
    Unknown error in space reserved for the JSONRPC specification
    """

    pass


class ParseError(JSONRPCError):
    """
    The server cannot parse the received JSON
    """

    pass


class InvalidRequest(JSONRPCError):
    """
    The server received an invalid Request object
    """

    pass


class MethodNotFound(JSONRPCError):
    """
    Method not found
    """

    pass


class InvalidParams(JSONRPCError):
    """
    Invalid method parameter(s) passed
    """

    pass


class InternalError(JSONRPCError):
    """
    Internal error
    """

    pass
