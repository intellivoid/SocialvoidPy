import time

class Request:
    def __init__(self, method, params=None, notification=False):
        self.method = method
        self.params = params
        self.id = str(time.monotonic()) if not notification else None
