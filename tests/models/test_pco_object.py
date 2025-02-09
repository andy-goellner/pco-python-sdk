from typing import Any, Mapping, cast
from planning_center_python.models.pco_object import PCOObject


TEST_DATA: Mapping[str, Any] = {
    "data": {
        "id": "foo",
        "type": "TestClass",
        "attributes": {"bar": "baz"},
        "relationships": {
            "test_relationship_key": {
                "data": {"type": "TestRelationship", "id": 12345}
            },
        },
    }
}


class TestRelationship(PCOObject):
    pass


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


def test_pco_object_relationships_returns_list():
    test_class = TestPCOObject(data=TEST_DATA)
    assert isinstance(test_class.relationships, list)


def test_pco_object_relationship_inits_class():
    test_class = TestPCOObject(data=TEST_DATA)
    assert isinstance(test_class.test_relationship, TestRelationship)  # type: ignore


def test_pco_object_inits_method():
    test_class = TestPCOObject(data=TEST_DATA)
    assert test_class.test_relationship.id == 12345  # type: ignore


def test_pco_object_sets_correct_defaults():
    test_class = TestPCOObject(data={"data": {"id": "foo", "type": "TestClass"}})
    assert test_class.attributes is None
    assert test_class.relationships == []
