from typing import List, Union
from pydantic import BaseModel

from pco_python.data.api_response._data import Data
from pco_python.data.api_response._meta import Meta


class Root(BaseModel):
    data: Union[Data, List[Data]]
    included: List[Data]
    meta: Meta
