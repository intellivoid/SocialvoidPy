from .general_error import GeneralError


class ValidationError(GeneralError):
    """
    Unknown validation error
    """

    pass


class InvalidUsername(ValidationError):
    """
    The given username is invalid and does not meet the specification
    """

    pass


class InvalidPassword(ValidationError):
    """
    The given password is insecure, see the message for further details
    """

    pass


class InvalidFirstName(ValidationError):
    """
    The first name provided contains invalid characters and/or is too long, see the message for further details
    """

    pass


class InvalidLastName(ValidationError):
    """
    The last name provided contains invalid characters and/or is too long, see the message for further details
    """

    pass


class InvalidBiography(ValidationError):
    """
    The biography provided contains invalid characters and/or is too long, see the message for further details
    """

    pass


class UsernameAlreadyExists(ValidationError):
    """
    The username is already registered in the network and cannot be used
    """

    pass


class InvalidPeerInput(ValidationError):
    """
    The client provided an invalid peer identification as input
    """

    pass


class InvalidPostText(ValidationError):
    """
    The post contains invalid characters and/or is too long, see the message for further details
    """

    pass


class InvalidClientPublicHash(ValidationError):
    """
    The client's public hash is invalid and cannot be identified as a sha256
    """

    pass


class InvalidClientPrivateHash(ValidationError):
    """
    The client's private hash is invalid and cannot be identified as a sha256
    """

    pass


class InvalidPlatform(ValidationError):
    """
    The platform name contains invalid characters and/or is too long, see the message for further details
    """

    pass


class InvalidVersion(ValidationError):
    """
    The version is invalid and/or is too long, see the message for further details
    """

    pass


class InvalidClientName(ValidationError):
    """
    The client name contains invalid characters and/or is too long, see the message for further details
    """

    pass


class InvalidSessionIdentification(ValidationError):
    """
    The session identification object is invalid, see the message for further details
    """

    pass


class InvalidFileForProfilePicture(ValidationError):
    """
    The given file is invalid for a profile picture
    """

    pass


class FileTooLarge(ValidationError):
    """
    The given file is too large to be processed
    """

    pass


class InvalidHelpDocumentId(ValidationError):
    """
    The given Help Document ID is invalid
    """

    pass


class AgreementRequired(ValidationError):
    """
    The client/user must agree to the condition to invoke the method
    """

    pass
