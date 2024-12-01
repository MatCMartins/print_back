import re
from src.modules.create_notification.app.create_notification_viewmodel import CreateNotificationViewModel
from src.shared.domain.entities.notification import Notification

class Test_CreateNotificationViewmodel:
    def test_create_notification_viewmodel(self):
        notification = Notification(
            notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            title="Enactus IMT",
            description="Enactus IMT is a student organization that aims to develop projects that help the community.",
            creation_date=123456789,
            has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
        )

        viewmodel = CreateNotificationViewModel(
            notification_id=notification.notification_id,
            title=notification.title,
            description=notification.description,
            creation_date=notification.creation_date,
            has_seen=notification.has_seen
        )

        assert re.match(r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$', viewmodel.to_dict()["notification_id"])

        expected = {
            "notification_id": notification.notification_id,
            "title": "Enactus IMT",
            "description": "Enactus IMT is a student organization that aims to develop projects that help the community.",
            "creation_date": 123456789,
            "has_seen": ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
        }	

        assert viewmodel.to_dict() == expected