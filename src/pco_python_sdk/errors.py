class BaseError(Exception):
    pass


class SignatureVerificationError(BaseError):
    def __init__(self, message: str, sig_header: str, body: str) -> None:
        super().__init__(message)
        self.sig_header = sig_header
        self.body = body
