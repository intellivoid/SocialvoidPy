from .general_error import GeneralError

class AuthenticationError(GeneralError):
    pass

class IncorrectLoginCredentials(AuthenticationError):
    pass

class IncorrectTwoFactorAuthenticationCode(AuthenticationError):
    pass

class AuthenticationNotApplicable(AuthenticationError):
    pass

class SessionNotFound(AuthenticationError):
    pass

class NotAuthenticated(AuthenticationError):
    pass

class PrivateAccessTokenRequired(AuthenticationError):
    pass

class AuthenticationFailure(AuthenticationError):
    pass

class BadSessionChallengeAnswer(AuthenticationError):
    pass

class TwoFactorAuthenticationRequired(AuthenticationError):
    pass

class AlreadyAuthenticated(AuthenticationError):
    pass

class SessionExpired(AuthenticationError):
    pass
