import pytest
from planning_center_python.errors import NoAttributesDefinedError
from planning_center_python.models.pco_object import PCOObject
from planning_center_python.models.person import Person


def test_object_url_returns_the_base_endpoint():
    assert Person(id="foo")._object_url() == "people/v2/people"  # type: ignore


def test_instance_url_includes_id():
    person = Person(id="foo")  # type: ignore
    assert person._instance_url() == "people/v2/people/foo"  # type: ignore


def test_person_is_a_pco_object():
    assert issubclass(Person, PCOObject)


def test_person_id_setter_sets_the_id():
    person = Person(id="foo")
    assert person.id == "foo"


def test_person_init_sets_type():
    person = Person(id="foo")
    assert person.type == "Person"


def test_data_sets_attributes():
    person = Person({"id": "foo", "type": "Person", "attributes": {"bar": "baz"}})
    assert person.id == "foo"
    assert person.type == "Person"
    assert person.attributes == {"bar": "baz"}


def test_get_attribute_returns_value():
    person = Person({"id": "foo", "type": "Person", "attributes": {"bar": "baz"}})
    assert person.get_attribute("bar") == "baz"


def test_get_attribute_raises_when_no_attributes_are_defined():
    person = Person(
        {
            "id": "foo",
            "type": "Person",
        }
    )
    with pytest.raises(NoAttributesDefinedError):
        person.get_attribute("foo")


def test_get_attribute_returns_none_when_attribute_missing():
    person = Person({"id": "foo", "type": "Person", "attributes": {"bar": "baz"}})
    assert person.get_attribute("not_existent") is None
