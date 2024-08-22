from pco_python_sdk.models._url_date_filter import UrlDateFilter


def test_url_filter_returns_formatted_dictionary():
    filter = UrlDateFilter("test_prop", ">", "some_value")
    assert filter.serialize() == {"where[test_prop][gt]": "some_value"}
