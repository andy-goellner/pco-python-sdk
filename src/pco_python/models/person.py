from datetime import date, datetime
from typing import Any, ClassVar, Literal, NotRequired, Self, TypedDict
from pco_python.errors import IdRequiredError
from pco_python.models._pagination_params import PaginationParams
from pco_python.models.pco_object import PCOObject


class Person(PCOObject):
    object_type: ClassVar[str] = "Person"

    class CreatePersonParams(TypedDict):
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

    class UpdatePersonParams(CreatePersonParams):
        pass

    class QueryPersonParams(TypedDict):
        accounting_administrator: NotRequired[bool]
        anniversary: NotRequired[date]
        birthdate: NotRequired[date]
        child: NotRequired[bool]
        created_at: NotRequired[datetime]
        first_name: NotRequired[str]
        gender: NotRequired[str]
        given_name: NotRequired[str]
        grade: NotRequired[int]
        graduation_year: NotRequired[int]
        id: NotRequired[str]
        inactivated_at: NotRequired[datetime]
        last_name: NotRequired[str]
        medical_notes: NotRequired[str]
        membership: NotRequired[str]
        mfa_configured: NotRequired[bool]
        middle_name: NotRequired[str]
        nickname: NotRequired[str]
        people_permissions: NotRequired[str]
        remote_id: NotRequired[int]
        search_name: NotRequired[str]
        search_name_or_email_or_phone_number: NotRequired[str]
        search_phone_number: NotRequired[str]
        search_phone_number_e164: NotRequired[str]
        site_administrator: NotRequired[bool]
        status: NotRequired[str]
        updated_at: NotRequired[datetime]

    class UrlParams(TypedDict):
        include: list[
            Literal[
                "addresses",
                "emails",
                "field_data",
                "households",
                "inactive_reason",
                "marital_status",
                "name_prefix",
                "name_suffix",
                "organization",
                "person_apps",
                "phone_numbers",
                "platform_notifications",
                "primary_campus",
                "school",
                "social_profiles",
            ]
        ]
        order: Literal[
            "accounting_administrator",
            "anniversary",
            "birthdate",
            "child",
            "given_name",
            "grade",
            "graduation_year",
            "last_name",
            "middle_name",
            "nickname",
            "people_permissions",
            "site_administrator",
            "gender",
            "inactivated_at",
            "created_at",
            "updated_at",
            "first_name",
            "remote_id",
            "membership",
            "status",
        ]
        pagination: PaginationParams
        # query_params:

    @classmethod
    def retrieve(cls, id: str, **params: Any) -> Self:
        instance = cls(**params)
        instance.id = id
        instance.refresh()
        return instance

    def get(self, id: str) -> None:
        self.id = id
        self.refresh()

    def create(self, params: CreatePersonParams) -> None:
        self._create_object(params)  # type: ignore

    def update(self, params: UpdatePersonParams) -> None:
        if not self.id:
            raise IdRequiredError(self)
        self._update_object(params)  # type: ignore

    def delete(self) -> None:
        self._delete_object()

    def object_url(self) -> str:
        return "people/v2/people"
