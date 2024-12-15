from typing import Any, Mapping

from pco_python.data.api_response._links import Links
from pco_python.data.api_response._pco_data_object import PcoDataObject
from pco_python.data.api_response._properties import Properties


class Data(PcoDataObject):
    properties: Properties
    relationships: Mapping[str, Any]
    links: Links
