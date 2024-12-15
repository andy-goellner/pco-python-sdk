from collections.abc import Mapping
from typing import List, Optional, Union
from pco_python.data.api_response._data import Data
from pco_python.data.api_response._links import Links
from pco_python.data.api_response._pco_data_object import PcoDataObject


class Relationships(Mapping[str, Data]):
    data: Optional[Union[PcoDataObject, List[PcoDataObject]]] = None
    links: Links
