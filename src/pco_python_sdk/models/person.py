from typing import Any, ClassVar, Self
from pco_python_sdk.models.pco_object import PCOObject


class Person(PCOObject):
    object_type: ClassVar[str] = "Person"

    @classmethod
    def retrieve(cls, id: str, **params: Any) -> Self:
        instance = cls(**params)
        instance.id = id
        instance.refresh()
        return instance

    def object_url(self) -> str:
        return "people/v2/people"
