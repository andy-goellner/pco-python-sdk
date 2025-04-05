from collections.abc import Mapping
from typing import Any
from planning_center_python.util.request_utils import format_params


def test_missing_include_returns_the_same_dict():
    original = {"foo": "bar"}
    assert original == format_params(original)


def test_empty_include_returns_the_same_dict():
    original: Mapping[str, Any] = {"foo": "bar", "include": []}
    assert original == format_params(original)


def test_one_item_in_include_returns_valid_dict():
    original: Mapping[str, Any] = {"foo": "bar", "include": ["emails"]}
    expected: Mapping[str, str] = {"foo": "bar", "include": "emails"}
    assert expected == format_params(original)


def test_multiple_items_in_include_returns_valid_dict():
    original: Mapping[str, Any] = {"foo": "bar", "include": ["emails", "addresses"]}
    expected: Mapping[str, str] = {"foo": "bar", "include": "emails,addresses"}
    assert expected == format_params(original)
