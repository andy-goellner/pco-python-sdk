from unittest.mock import MagicMock
import pytest
from pco_python_sdk.api import AbstractHttpClient
from pco_python_sdk.errors import RequestFailedError
from pco_python_sdk.models.pco_object import PCOObject
from pco_python_sdk.models.person import Person


def test_object_url_returns_the_base_endpoint():
    assert Person(client=object).object_url() == "people/v2/people"  # type: ignore


def test_instance_url_includes_id():
    person = Person(client=object)  # type: ignore
    person.id = "foo"
    assert person.instance_url() == "people/v2/people/foo"  # type: ignore


def test_person_is_a_pco_object():
    assert issubclass(Person, PCOObject)


def test_person_id_setter_sets_the_id():
    person = Person(client=object)  # type: ignore
    person.id = "foo"
    assert person.id == "foo"


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


def test_person_create_person_attributes_returns_a_dict():
    params = Person.CreatePersonParams(
        child=False, first_name="Daffy", last_name="Duck"
    )
    assert params == {"child": False, "first_name": "Daffy", "last_name": "Duck"}


def test_create_person_passes_attributes_to_client_as_dict(
    mocker: MagicMock, successful_client: AbstractHttpClient
):
    spy = mocker.spy(successful_client, "request")
    params = Person.CreatePersonParams(
        child=False, first_name="Daffy", last_name="Duck"
    )
    person = Person(client=successful_client)
    person.create(params)
    spy.assert_called_once_with(
        "post",
        "people/v2/people",
        payload={"child": False, "first_name": "Daffy", "last_name": "Duck"},
    )


def test_update_person_attributes_returns_a_dict():
    params = Person.UpdatePersonParams(
        child=False, first_name="Daffy", last_name="Duck"
    )
    assert params == {"child": False, "first_name": "Daffy", "last_name": "Duck"}


def test_update_person_passes_attributes_to_client_as_dict(
    mocker: MagicMock, successful_client: AbstractHttpClient
):
    spy = mocker.spy(successful_client, "request")
    params = Person.UpdatePersonParams(
        child=False, first_name="Daffy", last_name="Duck"
    )
    person = Person(client=successful_client)
    person.id = "foo"
    person.update(params)
    spy.assert_called_once_with(
        "patch",
        "people/v2/people/foo",
        payload={"child": False, "first_name": "Daffy", "last_name": "Duck"},
    )
