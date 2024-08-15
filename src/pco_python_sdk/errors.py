class BaseError(Exception):
    pass


class SignatureVerificationError(BaseError):
    def __init__(self, message: str, sig_header: str, body: str) -> None:
        super().__init__(message)
        self.sig_header = sig_header
        self.body = body


class InvalidRequestError(BaseError):
    pass


class RequestFailedError(BaseError):
    def __init__(self, message: str, status_code: int, *args: object) -> None:
        super().__init__(message)
        self.status_code = status_code
