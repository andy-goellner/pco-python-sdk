from planning_center_python.models.pco_object import PCOObject


class PersonApp(PCOObject):
    OBJECT_TYPE = "PersonApp"
    OBJECT_URL = "people/v2/person_apps"

    def _object_url(self) -> str:
        return self.OBJECT_URL
