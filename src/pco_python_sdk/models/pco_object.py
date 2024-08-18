from typing import Any, Dict, Self
from pco_python_sdk.api import AbstractHttpClient
from pco_python_sdk.errors import InvalidRequestError


class PCOObject:
    """Base class object from which all Planning Center objects should inherit from"""

    def __init__(self, client: AbstractHttpClient):
        self._client = client

    @classmethod
    def retrieve(cls, id: str, **params: Any) -> Self:
        raise NotImplementedError

    def get(self, id: str) -> None:
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
        """Makes a request to the API for the given object and refreshes
        the class properties.
        """
        response = self._client.request("get", self.instance_url())
        attributes = response.get("attributes")
        if attributes:
            self._refresh_props(attributes)

    def _refresh_props(self, props: Dict[str, Any]) -> None:
        """Sets a class properties for each value passed in.

        Args:
            props (Dict[str, Any]): a set of values for which a property should be generated
        """
        for k, v in props.items():
            setattr(self, k, v)

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        self._id = id
