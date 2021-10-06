from .general_error import GeneralError


class JSONRPCError(GeneralError):
    """
    Unknown error in space reserved for the JSONRPC specification
    """


class ParseError(JSONRPCError):
    """
    The server cannot parse the received JSON
    """


class InvalidRequest(JSONRPCError):
    """
    The server received an invalid Request object
    """


class MethodNotFound(JSONRPCError):
    """
    Method not found
    """


class InvalidParams(JSONRPCError):
    """
    Invalid method parameter(s) passed
    """


class InternalError(JSONRPCError):
    """
    Internal error
    """
