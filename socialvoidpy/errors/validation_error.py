from .general_error import GeneralError


class ValidationError(GeneralError):
    """
    Unknown validation error
    """


class InvalidUsername(ValidationError):
    """
    The given username is invalid and does not meet the specification
    """


class InvalidPassword(ValidationError):
    """
    The given password is insecure, see the message for further details
    """


class InvalidFirstName(ValidationError):
    """
    The first name provided contains invalid characters and/or is too long, see the message for further details
    """


class InvalidLastName(ValidationError):
    """
    The last name provided contains invalid characters and/or is too long, see the message for further details
    """


class InvalidBiography(ValidationError):
    """
    The biography provided contains invalid characters and/or is too long, see the message for further details
    """


class UsernameAlreadyExists(ValidationError):
    """
    The username is already registered in the network and cannot be used
    """


class InvalidPeerInput(ValidationError):
    """
    The client provided an invalid peer identification as input
    """


class InvalidPostText(ValidationError):
    """
    The post contains invalid characters and/or is too long, see the message for further details
    """


class InvalidClientPublicHash(ValidationError):
    """
    The client's public hash is invalid and cannot be identified as a sha256
    """


class InvalidClientPrivateHash(ValidationError):
    """
    The client's private hash is invalid and cannot be identified as a sha256
    """


class InvalidPlatform(ValidationError):
    """
    The platform name contains invalid characters and/or is too long, see the message for further details
    """


class InvalidVersion(ValidationError):
    """
    The version is invalid and/or is too long, see the message for further details
    """


class InvalidClientName(ValidationError):
    """
    The client name contains invalid characters and/or is too long, see the message for further details
    """


class InvalidSessionIdentification(ValidationError):
    """
    The session identification object is invalid, see the message for further details
    """


class InvalidFileForProfilePicture(ValidationError):
    """
    The given file is invalid for a profile picture
    """


class FileTooLarge(ValidationError):
    """
    The given file is too large to be processed
    """


class InvalidHelpDocumentId(ValidationError):
    """
    The given Help Document ID is invalid
    """


class AgreementRequired(ValidationError):
    """
    The client/user must agree to the condition to invoke the method
    """


class InvalidCursorValue(ValidationError):
    """
    The `cursor` parameter contains an invalid value. It cannot be under or equal to zero, see the message for further details
    """
