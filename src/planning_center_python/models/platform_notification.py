from planning_center_python.models.pco_object import PCOObject


class PlatformNotification(PCOObject):
    OBJECT_TYPE = "PlatformNotification"
    OBJECT_URL = "people/v2/platform_notifications"

    def _object_url(self) -> str:
        return self.OBJECT_URL
