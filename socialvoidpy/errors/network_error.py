from .general_error import GeneralError


class NetworkError(GeneralError):
    pass


class PeerNotFound(NetworkError):
    pass


class PostNotFound(NetworkError):
    pass


class PostDeleted(NetworkError):
    pass


class AlreadyReposted(NetworkError):
    pass


class FileUploadError(NetworkError):
    pass


class DocumentNotFound(NetworkError):
    pass


class AccessDenied(NetworkError):
    pass
