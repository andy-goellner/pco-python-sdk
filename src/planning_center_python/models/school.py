from planning_center_python.models.pco_object import PCOObject


class School(PCOObject):
    OBJECT_TYPE = "School"
    OBJECT_URL = "people/v2/schools"

    def _object_url(self) -> str:
        return self.OBJECT_URL
