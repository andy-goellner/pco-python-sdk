from planning_center_python.models.pco_object import PCOObject


class Organization(PCOObject):
    OBJECT_TYPE = "Organization"
    OBJECT_URL = "people/v2"

    def _object_url(self) -> str:
        return self.OBJECT_URL
