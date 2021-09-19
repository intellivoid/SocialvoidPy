from .general_error import GeneralError


class ValidationError(GeneralError):
    pass


class InvalidUsername(ValidationError):
    pass


class InvalidPassword(ValidationError):
    pass


class InvalidFirstName(ValidationError):
    pass


class InvalidLastName(ValidationError):
    pass


class InvalidBiography(ValidationError):
    pass


class UsernameAlreadyExists(ValidationError):
    pass


class InvalidPeerInput(ValidationError):
    pass


class InvalidPostText(ValidationError):
    pass


class InvalidClientPublicHash(ValidationError):
    pass


class InvalidClientPrivateHash(ValidationError):
    pass


class InvalidPlatform(ValidationError):
    pass


class InvalidVersion(ValidationError):
    pass


class InvalidClientName(ValidationError):
    pass


class InvalidSessionIdentification(ValidationError):
    pass


class InvalidFileForProfilePicture(ValidationError):
    pass


class FileTooLarge(ValidationError):
    pass


class InvalidHelpDocumentId(ValidationError):
    pass


class AgreementRequired(ValidationError):
    pass
