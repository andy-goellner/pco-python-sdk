from hashlib import sha256
import hmac
from typing import Any, Dict

from pco_python_sdk.errors import SignatureVerificationError

SIGNATURE_HEADER = "X-PCO-Webhooks-Authenticity"


class WebhookSignature(object):
    @staticmethod
    def _compute_signature(payload: str, secret: str) -> str:
        mac = hmac.new(
            secret.encode("utf-8"),
            msg=payload.encode("utf-8"),
            digestmod=sha256,
        )
        return mac.hexdigest()

    @staticmethod
    def _get_header_signature(header: Dict[str, Any]) -> Any | None:
        return header.get(SIGNATURE_HEADER)

    @classmethod
    def verify(cls, payload: str, headers: Dict[str, Any], secret: str) -> bool:
        try:
            signature = cls._get_header_signature(headers)
        except Exception:
            raise SignatureVerificationError(
                "Error parsing signature from header", "", payload
            )

        if not signature:
            raise SignatureVerificationError(
                "Could not find signature header", "", payload
            )

        if not isinstance(signature, str):
            raise SignatureVerificationError(
                "Invalid signature included in the headers", signature, payload
            )

        try:
            computed_signature = cls._compute_signature(payload, secret)
        except Exception:
            raise SignatureVerificationError(
                "Error computing signature", signature, payload
            )

        return hmac.compare_digest(signature, computed_signature)
