import pytest
from pco_python_sdk.api import AbstractHttpClient
from pco_python_sdk.errors import RequestFailedError
from pco_python_sdk.models.pco_object import PCOObject
from pco_python_sdk.models.person import Person


def test_endpoint_is_a_class_var():
    assert Person(id="foo").object_url() == "people/v2/people"


def test_endpoint_is_an_inst_var():
    assert Person(id="foo").instance_url() == "people/v2/people/foo"


def test_person_is_a_pco_object():
    assert issubclass(Person, PCOObject)


def test_person_retrieve_sets_the_id(successful_client: AbstractHttpClient):
    person = Person.retrieve(id="foo", client=successful_client)
    assert person.id == "foo"
    assert isinstance(person, Person)


def test_person_retrieve_error_is_raised(failed_client: AbstractHttpClient):
    with pytest.raises(RequestFailedError):
        Person.retrieve("foo", client=failed_client)


def test_person_retrieve_sets_properties(successful_client: AbstractHttpClient):
    person = Person.retrieve("foo", client=successful_client)
    assert person.fake_prop == "foobar"  # type: ignore
