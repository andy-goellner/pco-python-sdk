import pytest
from pco_python_sdk.errors import SignatureVerificationError
from pco_python_sdk.models.webhook_signature import WebhookSignature


SAMPLE_HEADERS = {
    "X-PCO-Webhooks-Event-ID": 1234567,
    "X-PCO-Webhooks-Event": "1sa1b1c-def1-ghi2-9876-123456acvb",
    "X-PCO-Webhooks-Name": "people.v2.events.thing.happened",
    "X-PCO-Webhooks-Event-Time": "2024-08-02T21:56:58Z",
    "X-PCO-Webhooks-Authenticity": "a7f2ea9fa2d645b4d2260f2885b939f0b6e3032edcec8e69b5b408fe682176e0",
    "Content-Type": "application/json",
}

SAMPLE_PAYLOAD = """{
  "data": [
    {
      "id": "1sa1b1c-def1-ghi2-9876-123456acvb",
      "type": "EventDelivery",
      "attributes": {
        "name": "people.v2.events.thing.happened",
        "attempt": 1,
        "payload": "{\"data\":{\"type\":\"Person\",\"id\":\"123\"}}"
      },
      "relationships": {
        "organization": {
          "data": {
            "type": "Organization",
            "id": "1234"
          }
        }
      }
    }
  ]
}"""

SAMPLE_SECRET = "abcdefg123456"


class TestWebhookSignature(object):
    def test_verify_decodes_correctly(self):
        assert (
            WebhookSignature.verify(SAMPLE_PAYLOAD, SAMPLE_HEADERS, SAMPLE_SECRET)
            is True
        )

    def test_verify_no_match_returns_false(self):
        headers = {"X-PCO-Webhooks-Authenticity": "abc123"}
        assert WebhookSignature.verify(SAMPLE_PAYLOAD, headers, SAMPLE_SECRET) is False

    def test_no_signature_raises_exception(self):
        headers = {"foo": "bar"}
        with pytest.raises(
            SignatureVerificationError, match="Could not find signature header"
        ):
            WebhookSignature.verify(SAMPLE_PAYLOAD, headers, SAMPLE_SECRET)

    def test_integer_header_raises_an_exception(self):
        headers = {"X-PCO-Webhooks-Authenticity": 12345}
        with pytest.raises(
            SignatureVerificationError,
            match="Invalid signature included in the headers",
        ):
            WebhookSignature.verify(SAMPLE_PAYLOAD, headers, SAMPLE_SECRET)

    def test_computed_signature_invalid_raises_error(self):
        secret = 123
        with pytest.raises(
            SignatureVerificationError,
            match="Error computing signature",
        ):
            WebhookSignature.verify(SAMPLE_PAYLOAD, SAMPLE_HEADERS, secret)  # type: ignore
