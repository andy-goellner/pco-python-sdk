from planning_center_python.models.pco_object import PCOObject


class Email(PCOObject):
    OBJECT_TYPE = "Email"
    OBJECT_URL = "people/v2/emails"

    def _object_url(self) -> str:
        return self.OBJECT_URL
