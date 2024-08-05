from pydantic import BaseModel

from pco_python_sdk.models.person_attributes import PersonAttributes


class Person(BaseModel):
    type: str = "Person"
    id: str
    attributes: PersonAttributes
