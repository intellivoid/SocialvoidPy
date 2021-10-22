from .general_error import *
from .jsonrpc_error import *
from .authentication_error import *
from .network_error import *
from .server_error import *
from .validation_error import *

ERROR_MAP = {
    # JSONRC Errors
    -32700: ParseError,
    -32600: InvalidRequest,
    -32601: MethodNotFound,
    -32602: InvalidParams,
    -32603: InternalError,
    # Authentication Errors
    8704: IncorrectLoginCredentials,
    8705: IncorrectTwoFactorAuthenticationCode,
    8706: AuthenticationNotApplicable,
    8707: SessionNotFound,
    8708: NotAuthenticated,
    8709: PrivateAccessTokenRequired,
    8710: AuthenticationFailure,
    8711: BadSessionChallengeAnswer,
    8712: TwoFactorAuthenticationRequired,
    8713: AlreadyAuthenticated,
    8714: SessionExpired,
    # Network Errors
    12544: PeerNotFound,
    12545: PostNotFound,
    12546: PostDeleted,
    12547: AlreadyReposted,
    12548: FileUploadError,
    12549: DocumentNotFound,
    12550: AccessDenied,
    12551: BlockedByPeer,
    12552: BlockedPeer,
    12553: SelfInteractionNotPermitted,
    # Server Errors
    16384: InternalServerError,
    16385: DocumentUpload,
    # Validation Errors
    8448: InvalidUsername,
    8449: InvalidPassword,
    8450: InvalidFirstName,
    8451: InvalidLastName,
    8452: InvalidBiography,
    8453: UsernameAlreadyExists,
    8454: InvalidPeerInput,
    8455: InvalidPostText,
    8456: InvalidClientPublicHash,
    8457: InvalidClientPrivateHash,
    8458: InvalidPlatform,
    8459: InvalidVersion,
    8460: InvalidClientName,
    8461: InvalidSessionIdentification,
    8462: InvalidFileForProfilePicture,
    8463: FileTooLarge,
    8464: InvalidHelpDocumentId,
    8465: AgreementRequired,
    8466: InvalidPageValue,
    8467: InvalidGeoLocation,
    8468: InvalidURLValue,
}
