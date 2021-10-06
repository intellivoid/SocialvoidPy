from .general_error import GeneralError


class NetworkError(GeneralError):
    """
    Unknown network error
    """

    pass


class PeerNotFound(NetworkError):
    """
    The requested user entity was not found in the network
    """

    pass


class PostNotFound(NetworkError):
    """
    Post not found
    """

    pass


class PostDeleted(NetworkError):
    """
    Post requested was deleted
    """

    pass


class AlreadyReposted(NetworkError):
    """
    Raised when trying to repost a post that's already been reposted
    """

    pass


class FileUploadError(NetworkError):
    """
    There was an error while trying to upload one or more files to the network
    """

    pass


class DocumentNotFound(NetworkError):
    """
    The requested Document ID was not found on the server
    """

    pass


class AccessDenied(NetworkError):
    """
    The authenticated peer does not have sufficient permissions to access the requested resource or to invoke a restricted method
    """

    pass
