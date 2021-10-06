from .general_error import GeneralError


class AuthenticationError(GeneralError):
    """
    Unknown authentication error
    """


class IncorrectLoginCredentials(AuthenticationError):
    """
    The given login credentials are incorrect
    """


class IncorrectTwoFactorAuthenticationCode(AuthenticationError):
    """
    The given two-factor authentication code is incorrect
    """


class AuthenticationNotApplicable(AuthenticationError):
    """
    The user does not support this method of authentication, see the message for further details
    """


class SessionNotFound(AuthenticationError):
    """
    The requested session was not found in the network
    """


class NotAuthenticated(AuthenticationError):
    """
    Method invoked requires authentication but session is not authenticated
    """


class PrivateAccessTokenRequired(AuthenticationError):
    """
    The user used a Private Access Token to authenticate and the client attempted to authenticate in another way
    """


class AuthenticationFailure(AuthenticationError):
    """
    The authentication process failed for some unexpected reason, see the message for further details
    """


class BadSessionChallengeAnswer(AuthenticationError):
    """
    The given session challenge answer is incorrect or out of sync
    """


class TwoFactorAuthenticationRequired(AuthenticationError):
    """
    Two-Factor Authentication is required, the client must repeat the same request but provide a Two-Factor authentication code as well
    """


class AlreadyAuthenticated(AuthenticationError):
    """
    The client is attempting to authenticate when already authenticated
    """


class SessionExpired(AuthenticationError):
    """
    Session expired
    """
