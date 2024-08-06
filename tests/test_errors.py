from pco_python_sdk.errors import SignatureVerificationError


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
