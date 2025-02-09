from typing import ClassVar

from planning_center_python.models.pco_object import PCOObject


class Gender(PCOObject):
    OBJECT_TYPE: ClassVar[str] = "Gender"
    OBJECT_URL: ClassVar[str] = "TBD"
