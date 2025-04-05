from typing import Any, Mapping, cast

import pytest
from planning_center_python.errors import InvalidParamsError, NoAttributesDefinedError
from planning_center_python.models.pco_object import PCOObject
from planning_center_python.types.inclusions import Inclusion


FAKE_DATA: Mapping[str, Any] = {
    "id": "foo",
    "type": "FakeClass",
    "attributes": {"bar": "baz"},
    "relationships": {
        "fake_relationship_key": {"data": {"type": "FakeRelationship", "id": 12345}},
    },
}


class FakeRelationship(PCOObject):
    pass


class FakeInclusion(PCOObject):
    OBJECT_TYPE = "FakeInclusion"


class FakePCOObject(PCOObject):
    OBJECT_TYPE = "FakeClass"
    RELATIONSHIPS = [
        {
            "type": "FakeRelationship",
            "method": "fake_relationship",
            "key": "fake_relationship_key",
            "association_type": "one",
            "klass": cast(PCOObject, FakeRelationship),
        }
    ]
    INCLUSION_DEFINITIONS = [
        {
            "type": "FakeInclusion",
            "method": "fake_inclusion",
            "key": "fake_inclusion_key",
            "association_type": "one",  # might not need this in inclusion so could invert the inheritance
            "klass": cast(PCOObject, FakeInclusion),
        }
    ]


class BadPCOObject(PCOObject):
    pass


def test_id_setter_sets_the_id():
    test_class = FakePCOObject(id="foo")
    assert test_class.id == "foo"


def test_person_init_sets_type():
    test_class = FakePCOObject(id="foo")
    assert test_class.type == "FakeClass"


def test_data_sets_attributes():
    test_class = FakePCOObject(
        {"id": "foo", "type": "FakeClass", "attributes": {"bar": "baz"}}
    )
    assert test_class.id == "foo"
    assert test_class.type == "FakeClass"
    assert test_class.attributes == {"bar": "baz"}


def test_get_attribute_raises_when_no_id_is_passed():
    with pytest.raises(InvalidParamsError):
        FakePCOObject({"type": "FakeClass"})


def test_get_attribute_raises_when_type_is_mismatched():
    with pytest.raises(InvalidParamsError):
        FakePCOObject({"id": 1234, "type": "NoType"})


def test_get_attribute_returns_value():
    test_class = FakePCOObject(
        {"id": "foo", "type": "FakeClass", "attributes": {"bar": "baz"}}
    )
    assert test_class.get_attribute("bar") == "baz"


def test_get_attribute_raises_when_no_attributes_are_defined():
    test_class = FakePCOObject({"id": "foo", "type": "FakeClass"})
    with pytest.raises(NoAttributesDefinedError):
        test_class.get_attribute("foo")


def test_get_attribute_returns_none_when_attribute_missing():
    test_class = FakePCOObject(
        {"id": "foo", "type": "FakeClass", "attributes": {"bar": "baz"}}
    )
    assert test_class.get_attribute("not_existent") is None


def test_pco_object_relationships_returns_list():
    test_class = FakePCOObject(data=FAKE_DATA)
    assert isinstance(test_class.relationships, list)


def test_pco_object_relationships_handles_null_object():
    test_class = FakePCOObject(
        data={
            "id": "foo",
            "type": "FakeClass",
            "attributes": {"bar": "baz"},
            "relationships": {
                "test_relationship_key": {"data": None},
            },
        }
    )
    assert test_class.relationships == []


def test_pco_object_relationship_inits_class():
    test_class = FakePCOObject(data=FAKE_DATA)
    assert isinstance(test_class.fake_relationship, FakeRelationship)  # type: ignore


def test_pco_object_inits_method():
    test_class = FakePCOObject(data=FAKE_DATA)
    assert test_class.fake_relationship.id == 12345  # type: ignore


def test_pco_object_get_relationship_returns_class():
    test_class = FakePCOObject(data=FAKE_DATA)
    relation = test_class.get_relationship("fake_relationship_key")
    assert isinstance(relation, FakeRelationship)
    assert relation.id == 12345


def test_pco_object_sets_correct_defaults():
    test_class = FakePCOObject(data={"id": "foo", "type": "FakeClass"})
    assert test_class.attributes is None
    assert test_class.relationships == []
    assert test_class.included == []


def test_pco_object_inits_inclusions():
    test_class = FakePCOObject(
        data={"id": "foo", "type": "FakeClass"},
        included_data=[
            {"id": 1234, "type": "FakeInclusion", "attributes": {"foo": "bar"}}
        ],
    )
    assert isinstance(test_class.included, list)
    assert len(test_class.included) == 1


def test_pco_object_inclusion_responds_to_method():
    test_class = FakePCOObject(
        data={"id": "foo", "type": "FakeClass"},
        included_data=[
            {"id": 1234, "type": "FakeInclusion", "attributes": {"foo": "bar"}}
        ],
    )
    assert isinstance(test_class.fake_inclusion, FakeInclusion)  # type: ignore
    assert test_class.fake_inclusion.id == 1234  # type: ignore
    assert test_class.fake_inclusion.get_attribute("foo") == "bar"  # type: ignore


def test_pco_object_get_inclusion_returns_class():
    test_class = FakePCOObject(
        data={"id": "foo", "type": "FakeClass"},
        included_data=[
            {"id": 1234, "type": "FakeInclusion", "attributes": {"foo": "bar"}}
        ],
    )
    inclusion = test_class.get_inclusion("fake_inclusion_key")
    assert isinstance(inclusion, FakeInclusion)
    assert inclusion.id == 1234


def test_pco_object_inclusion_returns_list_of_tuples():
    test_class = FakePCOObject(
        data={"id": "foo", "type": "FakeClass"},
        included_data=[
            {"id": 1234, "type": "FakeInclusion", "attributes": {"foo": "bar"}}
        ],
    )
    inclusions = test_class.included
    assert isinstance(inclusions, list)
    assert len(inclusions) == 1
    assert isinstance(inclusions[0], Inclusion)
    assert inclusions[0].key == "fake_inclusion_key"
