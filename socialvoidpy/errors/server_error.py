from .general_error import GeneralError


class ServerError(GeneralError):
    """
    Unknown server error
    """

    pass


class InternalServerError(ServerError):
    """
    An unexpected error occured while trying to process your request
    """

    pass


class DocumentUpload(ServerError):
    """
    An error occured while trying to process a document upload
    """

    pass
