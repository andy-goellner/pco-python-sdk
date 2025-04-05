from datetime import date, datetime
from typing import Optional, TypedDict, cast
from planning_center_python.models.address import Address
from planning_center_python.models.email import Email
from planning_center_python.models.field_datum import FieldDatum
from planning_center_python.models.gender import Gender
from planning_center_python.models.household import Household
from planning_center_python.models.inactive_reason import InactiveReason
from planning_center_python.models.marital_status import MaritalStatus
from planning_center_python.models.name_prefix import NamePrefix
from planning_center_python.models.name_suffix import NameSuffix
from planning_center_python.models.organization import Organization
from planning_center_python.models.pco_object import PCOObject
from planning_center_python.models.person_app import PersonApp
from planning_center_python.models.phone_number import PhoneNumber
from planning_center_python.models.platform_notification import PlatformNotification
from planning_center_python.models.primary_campus import PrimaryCampus
from planning_center_python.models.school import School
from planning_center_python.models.social_profile import SocialProfile
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
    INCLUSION_DEFINITIONS = [
        {
            "type": "Address",
            "method": "addresses",
            "key": "addresses",
            "association_type": "many",
            "klass": cast(AbstractPCOObject, Address),
        },
        {
            "type": "Email",
            "method": "emails",
            "key": "emails",
            "association_type": "many",
            "klass": cast(AbstractPCOObject, Email),
        },
        {
            "type": "FieldDatum",
            "method": "field_data",
            "key": "field_data",
            "association_type": "many",
            "klass": cast(AbstractPCOObject, FieldDatum),
        },
        {
            "type": "Household",
            "method": "households",
            "key": "households",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, Household),
        },
        {
            "type": "InactiveReason",
            "method": "inactive_reason",
            "key": "inactive_reason",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, InactiveReason),
        },
        {
            "type": "MaritalStatus",
            "method": "marital_status",
            "key": "marital_status",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, MaritalStatus),
        },
        {
            "type": "NamePrefix",
            "method": "name_prefix",
            "key": "name_prefix",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, NamePrefix),
        },
        {
            "type": "NameSuffix",
            "method": "name_suffix",
            "key": "name_suffix",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, NameSuffix),
        },
        {
            "type": "Organization",
            "method": "organization",
            "key": "organization",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, Organization),
        },
        {
            "type": "PersonApp",
            "method": "person_apps",
            "key": "person_apps",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, PersonApp),
        },
        {
            "type": "PhoneNumber",
            "method": "phone_numbers",
            "key": "phone_numbers",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, PhoneNumber),
        },
        {
            "type": "PlatformNotification",
            "method": "platform_notifications",
            "key": "platform_notifications",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, PlatformNotification),
        },
        {
            "type": "PrimaryCampus",
            "method": "primary_campus",
            "key": "primary_campus",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, PrimaryCampus),
        },
        {
            "type": "School",
            "method": "school",
            "key": "school",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, School),
        },
        {
            "type": "SocialProfile",
            "method": "social_profiles",
            "key": "social_profiles",
            "association_type": "one",
            "klass": cast(AbstractPCOObject, SocialProfile),
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
