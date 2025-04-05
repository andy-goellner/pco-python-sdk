from planning_center_python.models.pco_object import PCOObject


class NameSuffix(PCOObject):
    OBJECT_TYPE = "NameSuffix"
    OBJECT_URL = "people/v2/name_suffixes"

    def _object_url(self) -> str:
        return self.OBJECT_URL
