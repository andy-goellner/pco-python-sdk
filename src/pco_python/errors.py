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


class InvalidCredentialsError(BaseError):
    pass


class IdRequiredError(BaseError):
    def __init__(self, klass: object):
        message = f"Id required to make an update request for {type(klass).__name__}"
        super().__init__(message)
