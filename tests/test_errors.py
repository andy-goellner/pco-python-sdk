from planning_center_python.errors import (
    PCOClientInitializationError,
    SignatureVerificationError,
)


class TestSignatureError(object):
    def test_str_error(self):
        err = SignatureVerificationError("Test Message", "testsig", "testpayload")
        assert str(err) == "Test Message"

    def test_repr_error(self):
        err = SignatureVerificationError("Test Message", "testsig", "testpayload")
        assert repr(err) == "SignatureVerificationError('Test Message')"

    def test_sig_header_attribute_accessible(self):
        err = SignatureVerificationError("Test Message", "testsig", "testpayload")
        assert err.sig_header == "testsig"

    def test_payload_attribute_accessible(self):
        err = SignatureVerificationError("Test Message", "testsig", "testpayload")
        assert err.body == "testpayload"

    def test_pco_client_initialization_error(self):
        err = PCOClientInitializationError()
        assert (
            repr(err)
            == "PCOClientInitializationError('credentials or http_client are required to initialize PCOClient')"
        )
