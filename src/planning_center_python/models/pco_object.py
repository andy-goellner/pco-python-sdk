from collections.abc import Mapping
from typing import Any, ClassVar, Optional, cast

from planning_center_python.errors import (
    InvalidParamsError,
    InvalidRequestError,
    NoAttributesDefinedError,
)
from planning_center_python.types.abstract_pco_object import AbstractPCOObject
from planning_center_python.types.relationships import (
    Relationship,
    RelationshipDefinition,
)


class PCOObject(AbstractPCOObject):
    """Base class object from which all Planning Center objects should inherit from"""

    OBJECT_TYPE: ClassVar[str] = "BaseClass"
    OBJECT_URL: ClassVar[str] = ""
    RELATIONSHIPS: ClassVar[list[RelationshipDefinition]] = []

    def __call__(self, data: Mapping[str, Any] = {}, id: Optional[str] = None) -> Any:
        self.__init__(data=data, id=id)

    def __init__(self, data: Mapping[str, Any] = {}, id: Optional[str] = None):
        self._data = data
        object_data = cast(Mapping[str, Any], data.get("data")) or {}
        self._id = id or object_data.get("id")
        self._type = object_data.get("type") or self.OBJECT_TYPE
        self._validate()
        self.attributes = object_data.get("attributes")
        self.relationships = self._init_relationships(
            cast(Mapping[str, Any], object_data.get("relationships"))
        )

    def get_attribute(self, name: str) -> Any:
        if not self.attributes:
            raise NoAttributesDefinedError
        return self.attributes.get(name)

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

    def _init_relationships(self, object_data: Mapping[str, Any]) -> list[Relationship]:
        built_relationships: list[Relationship] = []
        if object_data:
            for definition in self.RELATIONSHIPS:
                relation = object_data.get(definition["key"])
                if relation:
                    relation_id = relation["data"]["id"]
                    klass_instance = definition["klass"](id=relation_id)
                    built_relationships.append(
                        Relationship(definition["association_type"], klass_instance)
                    )
                    self.__setattr__(definition["method"], klass_instance)
        return built_relationships

    @property
    def id(self) -> str | None:
        return self._id

    @property
    def type(self) -> str | None:
        return self._type
