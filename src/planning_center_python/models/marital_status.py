from planning_center_python.models.pco_object import PCOObject


class MaritalStatus(PCOObject):
    OBJECT_TYPE = "MaritalStatus"
    OBJECT_URL = "people/v2/marital_statuses"

    def _object_url(self) -> str:
        return self.OBJECT_URL
