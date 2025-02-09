from typing import NamedTuple, TypedDict
from planning_center_python.types.abstract_pco_object import AbstractPCOObject


class RelationshipDefinition(TypedDict):
    type: str
    method: str
    key: str
    association_type: str
    klass: AbstractPCOObject


class Relationship(NamedTuple):
    relationship_name: str
    class_instance: AbstractPCOObject
