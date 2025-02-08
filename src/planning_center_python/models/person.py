from datetime import date, datetime
from typing import Optional, TypedDict, cast
from planning_center_python.models.gender import Gender
from planning_center_python.models.pco_object import PCOObject
from planning_center_python.models.primary_campus import PrimaryCampus
from planning_center_python.types.abstract_pco_object import AbstractPCOObject


class Person(PCOObject):
    OBJECT_TYPE = "Person"
    OBJECT_URL = "people/v2/people"
    RELATIONSHIPS = [
        {
            "type": "Gender",
            "method": "gender",
            "key": "gender",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, Gender),
        },
        {
            "type": "PrimaryCampus",
            "method": "primary_campus",
            "key": "primary_campus",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, PrimaryCampus),
        },
    ]

    class CreatePersonParams(TypedDict):
        accounting_administrator: Optional[bool]
        anniversary: Optional[date]
        birthdate: Optional[date]
        child: Optional[bool]
        given_name: Optional[str]
        grade: Optional[int]
        graduation_year: Optional[int]
        last_name: Optional[str]
        middle_name: Optional[str]
        nickname: Optional[str]
        people_permission: Optional[str]
        site_administrator: Optional[bool]
        gender: Optional[str]
        inactivated_at: Optional[datetime]
        medical_notes: Optional[str]
        membership: Optional[str]
        avatar: Optional[str]
        first_name: Optional[str]
        gender_id: Optional[str]
        primary_campus_id: Optional[str]
        remote_id: Optional[int]
        status: Optional[str]

    class UpdatePersonParams(CreatePersonParams):
        pass

    class QueryPersonParams(TypedDict):
        accounting_administrator: Optional[bool]
        anniversary: Optional[date]
        birthdate: Optional[date]
        child: Optional[bool]
        created_at: Optional[datetime]
        first_name: Optional[str]
        gender: Optional[str]
        given_name: Optional[str]
        grade: Optional[int]
        graduation_year: Optional[int]
        id: Optional[str]
        inactivated_at: Optional[datetime]
        last_name: Optional[str]
        medical_notes: Optional[str]
        membership: Optional[str]
        mfa_configured: Optional[bool]
        middle_name: Optional[str]
        nickname: Optional[str]
        people_permissions: Optional[str]
        remote_id: Optional[int]
        search_name: Optional[str]
        search_name_or_email_or_phone_number: Optional[str]
        search_phone_number: Optional[str]
        search_phone_number_e164: Optional[str]
        site_administrator: Optional[bool]
        status: Optional[str]
        updated_at: Optional[datetime]

    def _object_url(self) -> str:
        return self.OBJECT_URL
