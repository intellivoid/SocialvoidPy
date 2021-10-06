from .general_error import GeneralError


class NetworkError(GeneralError):
    """
    Unknown network error
    """


class PeerNotFound(NetworkError):
    """
    The requested user entity was not found in the network
    """


class PostNotFound(NetworkError):
    """
    Post not found
    """


class PostDeleted(NetworkError):
    """
    Post requested was deleted
    """


class AlreadyReposted(NetworkError):
    """
    Raised when trying to repost a post that's already been reposted
    """


class FileUploadError(NetworkError):
    """
    There was an error while trying to upload one or more files to the network
    """


class DocumentNotFound(NetworkError):
    """
    The requested Document ID was not found on the server
    """


class AccessDenied(NetworkError):
    """
    The authenticated peer does not have sufficient permissions to access the requested resource or to invoke a restricted method
    """
