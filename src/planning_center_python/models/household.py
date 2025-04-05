from planning_center_python.models.pco_object import PCOObject


class Household(PCOObject):
    OBJECT_TYPE = "Household"
    OBJECT_URL = "people/v2/households"

    def _object_url(self) -> str:
        return self.OBJECT_URL
