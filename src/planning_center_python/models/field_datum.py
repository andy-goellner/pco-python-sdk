from planning_center_python.models.pco_object import PCOObject


class FieldDatum(PCOObject):
    OBJECT_TYPE = "FieldDatum"
    OBJECT_URL = "people/v2/field_data"

    def _object_url(self) -> str:
        return self.OBJECT_URL
