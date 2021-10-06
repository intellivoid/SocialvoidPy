from .general_error import GeneralError


class AuthenticationError(GeneralError):
    """
    Unknown authentication error
    """

    pass


class IncorrectLoginCredentials(AuthenticationError):
    """
    The given login credentials are incorrect
    """

    pass


class IncorrectTwoFactorAuthenticationCode(AuthenticationError):
    """
    The given two-factor authentication code is incorrect
    """

    pass


class AuthenticationNotApplicable(AuthenticationError):
    """
    The user does not support this method of authentication, see the message for further details
    """

    pass


class SessionNotFound(AuthenticationError):
    """
    The requested session was not found in the network
    """

    pass


class NotAuthenticated(AuthenticationError):
    """
    Method invoked requires authentication but session is not authenticated
    """

    pass


class PrivateAccessTokenRequired(AuthenticationError):
    """
    The user used a Private Access Token to authenticate and the client attempted to authenticate in another way
    """

    pass


class AuthenticationFailure(AuthenticationError):
    """
    The authentication process failed for some unexpected reason, see the message for further details
    """

    pass


class BadSessionChallengeAnswer(AuthenticationError):
    """
    The given session challenge answer is incorrect or out of sync
    """

    pass


class TwoFactorAuthenticationRequired(AuthenticationError):
    """
    Two-Factor Authentication is required, the client must repeat the same request but provide a Two-Factor authentication code as well
    """

    pass


class AlreadyAuthenticated(AuthenticationError):
    """
    The client is attempting to authenticate when already authenticated
    """

    pass


class SessionExpired(AuthenticationError):
    """
    Session expired
    """

    pass
