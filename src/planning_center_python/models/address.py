from planning_center_python.models.pco_object import PCOObject


class Address(PCOObject):
    OBJECT_TYPE = "Address"
    OBJECT_URL = "people/v2/addresses"

    def _object_url(self) -> str:
        return self.OBJECT_URL
