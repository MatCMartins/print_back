from typing import List, Optional

from src.shared.domain.entities.notification import Notification
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.notification_repository_interface import INotificationRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class NotificationRepositoryMock(INotificationRepository):
    notifications: List[Notification]

    def __init__(self):
        self.notifications = [
            Notification(
                notification_id="7d644e62-ef8b-4728-a92b-becb8930c24e",
                title="Data Science Club IMT", 
                description="Organization dedicated to promoting knowledge and projects in the field of data science and machine learning.", 
                creation_date=1620009600,
                has_seen=["7d644e62-ef8b-4728-a92b-becb8930c24e"]

            ),
            Notification(
                notification_id="7d644e62-ef8b-4728-a92b-becb8930c24e",
                title="AI Lab Mauá", 
                description="A community focused on artificial intelligence research and applications, encouraging students to participate in AI projects.", 
                creation_date=1609459200,
                has_seen=["7d644e62-ef8b-4728-a92b-becb8930c24e"]

            ),
            Notification(
                notification_id="7d644e62-ef8b-4728-a92b-becb8930c24e",
                title="Robotics Team Mauá", 
                description="A student organization focused on building and programming autonomous robots to compete in national and international competitions.", 
                creation_date=1619827200,
                has_seen=["7d644e62-ef8b-4728-a92b-becb8930c24e"]

            )
        ]

    def get_notification(self, notification_id: str) -> Notification:
        for notification in self.notifications:
            if notification.notification_id == notification_id:
                return notification
        return None

    def get_all_notifications(self) -> List[Notification]:
        return self.notifications

    def create_notification(self, new_notification: Notification) -> Notification:
        self.notifications.append(new_notification)
        return new_notification

    def delete_notification(self, notification_id: str) -> Notification:
        for idx, notification in enumerate(self.notifications):
            if notification.notification_id == notification_id:
                return self.notifications.pop(idx)

        return None

    def update_notification(self, notification_id: str, new_title: Optional[str] = None, new_description: Optional[str] = None, new_creation_date: int = None, new_has_seen: list = None) -> Notification:
        for notification in self.notifications:
            if notification.notification_id == notification_id:
                if new_title is not None:
                    notification.title = new_title
                if new_description is not None:
                    notification.description = new_description
                if new_creation_date is not None:
                    notification.creation_date = new_creation_date
                if new_has_seen is not None:
                    notification.has_seen = new_has_seen
                return notification

        return None
