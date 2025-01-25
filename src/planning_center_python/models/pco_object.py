from collections.abc import Mapping
from typing import Any, ClassVar, Optional, cast
from planning_center_python.errors import (
    InvalidParamsError,
    InvalidRequestError,
    NoAttributesDefinedError,
)


class PCOObject:
    """Base class object from which all Planning Center objects should inherit from"""

    OBJECT_TYPE: ClassVar[str] = "BaseClass"

    def __init__(self, data: Mapping[str, Any] = {}, id: Optional[str] = None):
        self._data = data
        object_data = cast(Mapping[str, Any], data.get("data")) or {}
        self._id = id or object_data.get("id")
        self._type = object_data.get("type") or self.OBJECT_TYPE
        self._validate()
        self.attributes = object_data.get("attributes")

    def get_attribute(self, name: str) -> Any:
        if not self.attributes:
            raise NoAttributesDefinedError
        return self.attributes.get(name)

    def _object_url(self) -> str:
        raise NotImplementedError

    def _instance_url(self) -> str:
        if not self.id:
            raise InvalidRequestError(
                "Cannot determine instance url without a valid id"
            )

        return "%s/%s" % (self._object_url(), self.id)

    def _validate(self):
        if not self.id:
            raise InvalidParamsError(self, "id")
        if not self.type:
            raise InvalidParamsError(self, "type")
        if self.type != self.OBJECT_TYPE:
            raise InvalidParamsError(self, "type", "Class types do not match")

    def _init_attributes(self, attributes: Mapping[str, Any]):
        for key, val in attributes.items():
            setattr(self, key, val)

    @property
    def id(self) -> str | None:
        return self._id

    @property
    def type(self) -> str | None:
        return self._type
