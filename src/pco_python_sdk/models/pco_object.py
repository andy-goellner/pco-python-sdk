from typing import Any, Dict, Optional, Self
from pco_python_sdk.api import AbstractClient, Client
from pco_python_sdk.errors import InvalidRequestError


class PCOObject:
    def __init__(self, id: str, client: Optional[AbstractClient] = None):
        self.id = id
        self._client = Client() if client is None else client

    @classmethod
    def retrieve(cls, id: str) -> Self:
        raise NotImplementedError

    def object_url(self) -> str:
        raise NotImplementedError

    def instance_url(self) -> str:
        if not self.id:
            raise InvalidRequestError(
                "Cannot determine instance url without a valid id"
            )

        return "%s/%s" % (self.object_url(), self.id)

    def refresh(self) -> None:
        response = self._client.request("get", self.instance_url())
        attributes = response.get("attributes")
        if attributes:
            self._refresh_props(attributes)

    def _refresh_props(self, props: Dict[str, Any]) -> None:
        for k, v in props.items():
            setattr(self, k, v)
