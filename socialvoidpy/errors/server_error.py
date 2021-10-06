from .general_error import GeneralError


class ServerError(GeneralError):
    """
    Unknown server error
    """


class InternalServerError(ServerError):
    """
    An unexpected error occured while trying to process your request
    """


class DocumentUpload(ServerError):
    """
    An error occured while trying to process a document upload
    """
