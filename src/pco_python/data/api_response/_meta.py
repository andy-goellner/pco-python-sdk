from typing import List
from pydantic import BaseModel

from pco_python.data.api_response._parent import Parent


class Meta(BaseModel):
    can_include: List[str]
    parent: Parent
