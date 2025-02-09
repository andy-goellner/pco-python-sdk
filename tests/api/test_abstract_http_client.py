import pytest

from planning_center_python.api.abstract_http_client import AbstractHttpClient


def test_abstract_class_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        AbstractHttpClient().request("foo", "bar")
