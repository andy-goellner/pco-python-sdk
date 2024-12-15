from abc import ABC
from typing import Any, Dict

from pco_python.data.api_response.pco_response import PCOResponse


class AbstractHttpClient(ABC):
    """Abstract base class representation for the HTTP client. Should be inherited and overridden."""

    def request(
        self,
        verb: str,
        endpoint: str,
        query: Dict[str, str] = {},
        payload: Dict[str, Any] = {},
        headers: Dict[str, str] = {},
    ) -> PCOResponse:
        raise NotImplementedError
