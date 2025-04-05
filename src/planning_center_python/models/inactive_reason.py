from planning_center_python.models.pco_object import PCOObject


class InactiveReason(PCOObject):
    OBJECT_TYPE = "InactiveReason"
    OBJECT_URL = "people/v2/inactive_reasons"

    def _object_url(self) -> str:
        return self.OBJECT_URL
