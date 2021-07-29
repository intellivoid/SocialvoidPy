class Response:
    def __init__(self, body):
        self.id = body['id']
        self.success = 'error' not in body
        self.data = body.get('result')
        self.error = body.get('error')
        self.raw = body
