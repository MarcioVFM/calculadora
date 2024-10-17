class HttpUnprocessebleEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessebleEntity'
        self.status_code = 422