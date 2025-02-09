from collections.abc import Mapping
from typing import Any, ClassVar, Optional, cast

from planning_center_python.errors import (
    InvalidParamsError,
    InvalidRequestError,
    NoAttributesDefinedError,
)
from planning_center_python.types.abstract_pco_object import AbstractPCOObject
from planning_center_python.types.inclusions import Inclusion, InclusionDefinition
from planning_center_python.types.relationships import (
    Relationship,
    RelationshipDefinition,
)


class PCOObject(AbstractPCOObject):
    """Base class object from which all Planning Center objects should inherit from"""

    OBJECT_TYPE: ClassVar[str] = "BaseClass"
    OBJECT_URL: ClassVar[str] = ""
    RELATIONSHIPS: ClassVar[list[RelationshipDefinition]] = []
    INCLUSION_DEFINITIONS: ClassVar[list[InclusionDefinition]] = []

    def __call__(
        self,
        data: Mapping[str, Any] = {},
        id: Optional[str] = None,
        included_data: list[Mapping[str, Any]] = [],
    ) -> Any:
        self.__init__(data=data, id=id)

    def __init__(
        self,
        data: Mapping[str, Any] = {},
        id: Optional[str] = None,
        included_data: list[Mapping[str, Any]] = [],
    ):
        self._data = data
        self._id = id or data.get("id")
        self._type = data.get("type") or self.OBJECT_TYPE
        self._validate()
        self.attributes = data.get("attributes")
        self.relationships = self._init_relationships(
            cast(Mapping[str, Any], data.get("relationships"))
        )
        self.included = self._init_inclusions(included_data)

    def get_attribute(self, name: str) -> Any:
        if not self.attributes:
            raise NoAttributesDefinedError
        return self.attributes.get(name)

    def get_relationship(self, key: str) -> AbstractPCOObject | None:
        return next(
            (r.class_instance for r in self.relationships if r.key == key),
            None,
        )

    def get_inclusion(self, key: str) -> AbstractPCOObject | None:
        return next(
            (r.class_instance for r in self.included if r.key == key),
            None,
        )

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

    def _init_relationships(
        self, object_data: Mapping[str, Any] | None
    ) -> list[Relationship]:
        built_relationships: list[Relationship] = []
        if object_data:
            for definition in self.RELATIONSHIPS:
                relation = object_data.get(definition["key"])
                if relation:
                    relation_id = relation["data"]["id"]
                    klass_instance = definition["klass"](id=relation_id)
                    built_relationships.append(
                        Relationship(definition["key"], klass_instance)
                    )
                    self.__setattr__(definition["method"], klass_instance)
        return built_relationships

    def _init_inclusions(
        self, included_data: list[Mapping[str, Any]] | None
    ) -> list[Inclusion]:
        built_inclusions: list[Inclusion] = []
        if included_data:
            for inclusion in included_data:
                definition = self._find_definition_from_type(
                    self.INCLUSION_DEFINITIONS, inclusion["type"]
                )
                if definition:
                    klass_instance = definition["klass"](data=inclusion)
                    built_inclusions.append(
                        Inclusion(definition["key"], klass_instance)
                    )
                    self.__setattr__(definition["method"], klass_instance)

        return built_inclusions

    @staticmethod
    def _find_definition_from_type(
        definitions: list[RelationshipDefinition | InclusionDefinition], def_type: str
    ) -> InclusionDefinition | RelationshipDefinition | None:
        return next((dfn for dfn in definitions if dfn["type"] == def_type), None)

    @property
    def id(self) -> str | None:
        return self._id

    @property
    def type(self) -> str | None:
        return self._type
