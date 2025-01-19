from planning_center_python.models._url_params_base import UrlParamsBase


def test_url_params_include_returns_comma_delim_string():
    params = UrlParamsBase(include=["person", "household", "phone_number"])
    assert params.serialize() == {"include": "person,household,phone_number"}


def test_url_params_order_returns_dict_attributes():
    params = UrlParamsBase(order="last_name")
    assert params.serialize() == {"order": "last_name"}
