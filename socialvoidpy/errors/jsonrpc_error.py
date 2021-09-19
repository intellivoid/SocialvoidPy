from .general_error import GeneralError


class JSONRPCError(GeneralError):
    pass


class ParseError(JSONRPCError):
    pass


class InvalidRequest(JSONRPCError):
    pass


class MethodNotFound(JSONRPCError):
    pass


class InvalidParams(JSONRPCError):
    pass


class InternalError(JSONRPCError):
    pass
