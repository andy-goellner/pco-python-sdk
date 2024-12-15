from pydantic import BaseModel


class PcoDataObject(BaseModel):
    type: str
    id: str
