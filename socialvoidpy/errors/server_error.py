from .general_error import GeneralError


class ServerError(GeneralError):
    pass


class InternalServerError(ServerError):
    pass


class DocumentUpload(ServerError):
    pass
