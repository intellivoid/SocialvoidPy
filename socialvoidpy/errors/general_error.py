class GeneralError(Exception):
    def __init__(self, code, message, data):
        super().__init__(message)
        self.code = code
        self.data = data

# Can this go somewhere else?
class SessionDoesNotExist(GeneralError):
    pass
