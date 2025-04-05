from planning_center_python.models.pco_object import PCOObject


class SocialProfile(PCOObject):
    OBJECT_TYPE = "SocialProfile"
    OBJECT_URL = "people/v2/social_profiles"

    def _object_url(self) -> str:
        return self.OBJECT_URL
