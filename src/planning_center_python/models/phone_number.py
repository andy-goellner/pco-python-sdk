from planning_center_python.models.pco_object import PCOObject


class PhoneNumber(PCOObject):
    OBJECT_TYPE = "PhoneNumber"
    OBJECT_URL = "people/v2/phone_numbers"

    def _object_url(self) -> str:
        return self.OBJECT_URL
