from src.modules.delete_notification.app.delete_notification_viewmodel import DeleteNotificationViewmodel
from src.shared.domain.entities.notification import Notification


class Test_DeleteNotificationViewmodel:
    def test_delete_notification_viewmodel(self):
        notification = Notification(
            notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            title="title",
            description="description",
            creation_date=1,
            has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
        )

        viewmodel = DeleteNotificationViewmodel(
            notification_id=notification.notification_id,
            title=notification.title,
            description=notification.description,
            creation_date=notification.creation_date,
            has_seen=notification.has_seen
        ).to_dict()

        expected = {
            "notification_id": notification.notification_id,
            "title": notification.title,
            "description": notification.description,
            "creation_date": notification.creation_date,
            "has_seen": notification.has_seen
        }	

        assert viewmodel == expected
