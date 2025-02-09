from typing import Any, Mapping, cast

import pytest
from planning_center_python.errors import InvalidParamsError, NoAttributesDefinedError
from planning_center_python.models.pco_object import PCOObject
from planning_center_python.types.inclusions import Inclusion


TEST_DATA: Mapping[str, Any] = {
    "id": "foo",
    "type": "TestClass",
    "attributes": {"bar": "baz"},
    "relationships": {
        "test_relationship_key": {"data": {"type": "TestRelationship", "id": 12345}},
    },
}


class TestRelationship(PCOObject):
    pass


class TestInclusion(PCOObject):
    OBJECT_TYPE = "TestInclusion"


class TestPCOObject(PCOObject):
    OBJECT_TYPE = "TestClass"
    RELATIONSHIPS = [
        {
            "type": "TestRelationship",
            "method": "test_relationship",
            "key": "test_relationship_key",
            "association_type": "one",
            "klass": cast(PCOObject, TestRelationship),
        }
    ]
    INCLUSION_DEFINITIONS = [
        {
            "type": "TestInclusion",
            "method": "test_inclusion",
            "key": "test_inclusion_key",
            "association_type": "one",  # might not need this in inclusion so could invert the inheritance
            "klass": cast(PCOObject, TestInclusion),
        }
    ]


class BadPCOObject(PCOObject):
    pass


def test_id_setter_sets_the_id():
    test_class = TestPCOObject(id="foo")
    assert test_class.id == "foo"


def test_person_init_sets_type():
    test_class = TestPCOObject(id="foo")
    assert test_class.type == "TestClass"


def test_data_sets_attributes():
    test_class = TestPCOObject(
        {"id": "foo", "type": "TestClass", "attributes": {"bar": "baz"}}
    )
    assert test_class.id == "foo"
    assert test_class.type == "TestClass"
    assert test_class.attributes == {"bar": "baz"}


def test_get_attribute_raises_when_no_id_is_passed():
    with pytest.raises(InvalidParamsError):
        TestPCOObject({"type": "TestClass"})


def test_get_attribute_raises_when_type_is_mismatched():
    with pytest.raises(InvalidParamsError):
        TestPCOObject({"id": 1234, "type": "NoType"})


def test_get_attribute_returns_value():
    test_class = TestPCOObject(
        {"id": "foo", "type": "TestClass", "attributes": {"bar": "baz"}}
    )
    assert test_class.get_attribute("bar") == "baz"


def test_get_attribute_raises_when_no_attributes_are_defined():
    test_class = TestPCOObject({"id": "foo", "type": "TestClass"})
    with pytest.raises(NoAttributesDefinedError):
        test_class.get_attribute("foo")


def test_get_attribute_returns_none_when_attribute_missing():
    test_class = TestPCOObject(
        {"id": "foo", "type": "TestClass", "attributes": {"bar": "baz"}}
    )
    assert test_class.get_attribute("not_existent") is None


def test_pco_object_relationships_returns_list():
    test_class = TestPCOObject(data=TEST_DATA)
    assert isinstance(test_class.relationships, list)


def test_pco_object_relationship_inits_class():
    test_class = TestPCOObject(data=TEST_DATA)
    assert isinstance(test_class.test_relationship, TestRelationship)  # type: ignore


def test_pco_object_inits_method():
    test_class = TestPCOObject(data=TEST_DATA)
    assert test_class.test_relationship.id == 12345  # type: ignore


def test_pco_object_get_relationship_returns_class():
    test_class = TestPCOObject(data=TEST_DATA)
    relation = test_class.get_relationship("test_relationship_key")
    assert isinstance(relation, TestRelationship)
    assert relation.id == 12345


def test_pco_object_sets_correct_defaults():
    test_class = TestPCOObject(data={"id": "foo", "type": "TestClass"})
    assert test_class.attributes is None
    assert test_class.relationships == []
    assert test_class.included == []


def test_pco_object_inits_inclusions():
    test_class = TestPCOObject(
        data={"id": "foo", "type": "TestClass"},
        included_data=[
            {"id": 1234, "type": "TestInclusion", "attributes": {"foo": "bar"}}
        ],
    )
    assert isinstance(test_class.included, list)
    assert len(test_class.included) == 1


def test_pco_object_inclusion_responds_to_method():
    test_class = TestPCOObject(
        data={"id": "foo", "type": "TestClass"},
        included_data=[
            {"id": 1234, "type": "TestInclusion", "attributes": {"foo": "bar"}}
        ],
    )
    assert isinstance(test_class.test_inclusion, TestInclusion)  # type: ignore
    assert test_class.test_inclusion.id == 1234  # type: ignore
    assert test_class.test_inclusion.get_attribute("foo") == "bar"  # type: ignore


def test_pco_object_get_inclusion_returns_class():
    test_class = TestPCOObject(
        data={"id": "foo", "type": "TestClass"},
        included_data=[
            {"id": 1234, "type": "TestInclusion", "attributes": {"foo": "bar"}}
        ],
    )
    inclusion = test_class.get_inclusion("test_inclusion_key")
    assert isinstance(inclusion, TestInclusion)
    assert inclusion.id == 1234


def test_pco_object_inclusion_returns_list_of_tuples():
    test_class = TestPCOObject(
        data={"id": "foo", "type": "TestClass"},
        included_data=[
            {"id": 1234, "type": "TestInclusion", "attributes": {"foo": "bar"}}
        ],
    )
    inclusions = test_class.included
    assert isinstance(inclusions, list)
    assert len(inclusions) == 1
    assert isinstance(inclusions[0], Inclusion)
    assert inclusions[0].key == "test_inclusion_key"
