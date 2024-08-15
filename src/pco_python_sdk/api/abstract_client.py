from abc import ABC
from typing import Any, Dict


class AbstractClient(ABC):
    def request(
        self,
        verb: str,
        endpoint: str,
        query: Dict[str, str] = {},
        payload: Dict[str, Any] = {},
        headers: Dict[str, str] = {},
    ) -> Dict[str, Any]:
        raise NotImplementedError
