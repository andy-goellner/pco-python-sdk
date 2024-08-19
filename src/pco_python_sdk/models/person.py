from datetime import date, datetime
from typing import Any, ClassVar, NotRequired, Self, TypedDict
from pco_python_sdk.errors import IdRequiredError
from pco_python_sdk.models.pco_object import PCOObject


class Person(PCOObject):
    object_type: ClassVar[str] = "Person"

    class UpdatePersonParams(TypedDict):
        accounting_administrator: NotRequired[bool]
        anniversary: NotRequired[date]
        birthdate: NotRequired[date]
        child: NotRequired[bool]
        given_name: NotRequired[str]
        grade: NotRequired[int]
        graduation_year: NotRequired[int]
        last_name: NotRequired[str]
        middle_name: NotRequired[str]
        nickname: NotRequired[str]
        people_permission: NotRequired[str]
        site_administrator: NotRequired[bool]
        gender: NotRequired[str]
        inactivated_at: NotRequired[datetime]
        medical_notes: NotRequired[str]
        membership: NotRequired[str]
        avatar: NotRequired[str]
        first_name: NotRequired[str]
        gender_id: NotRequired[str]
        primary_campus_id: NotRequired[str]
        remote_id: NotRequired[int]
        status: NotRequired[str]

    @classmethod
    def retrieve(cls, id: str, **params: Any) -> Self:
        instance = cls(**params)
        instance.id = id
        instance.refresh()
        return instance

    def get(self, id: str) -> None:
        self.id = id
        self.refresh()

    def update(self, params: UpdatePersonParams):
        if not self.id:
            raise IdRequiredError(self)
        self._update_object(params)  # type: ignore

    def object_url(self) -> str:
        return "people/v2/people"
