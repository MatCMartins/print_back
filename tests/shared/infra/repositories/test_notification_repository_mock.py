from src.shared.domain.entities.notification import Notification
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.notification_repository_mock import NotificationRepositoryMock
import pytest


class Test_NotificationsRepositoryMock:
    def test_get_notification(self):
        repo = NotificationRepositoryMock()
        notification = repo.get_notification(repo.notifications[0].notification_id)

        assert notification.title == "Data Science Club IMT"
        assert notification.description == "Organization dedicated to promoting knowledge and projects in the field of data science and machine learning."
        assert notification.creation_date == 1620009600
        assert notification.has_seen == ["7d644e62-ef8b-4728-a92b-becb8930c24e"]

    def test_get_notification_not_found(self):
        repo = NotificationRepositoryMock()
        assert repo.get_notification(32) == None

    def test_get_all_notifications(self):
        repo = NotificationRepositoryMock()
        notifications = repo.get_all_notifications()
        assert len(notifications) == 3

    def test_create_notification(self):
        repo = NotificationRepositoryMock()
        notification = Notification(
            notification_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            title="Maua Tech",
            description="Technology organization focused on promoting knowledge and projects in the field of technology and innovation.",
            creation_date=1620009600,
            has_seen=["7d644e62-ef8b-4728-a92b-becb8930c24e"]

        )

        repo.create_notification(notification)

        assert repo.notifications[3].title == "Maua Tech"
        assert repo.notifications[3].description == "Technology organization focused on promoting knowledge and projects in the field of technology and innovation."
        assert repo.notifications[3].creation_date == 1620009600
        assert repo.notifications[3].has_seen == ["7d644e62-ef8b-4728-a92b-becb8930c24e"]

    def test_delete_notification(self):
        repo = NotificationRepositoryMock()
        notification = repo.delete_notification(notification_id=repo.notifications[0].notification_id)

        assert notification.title == "Data Science Club IMT"
        assert len(repo.notifications) == 2

    def test_delete_notification_not_found(self):
        repo = NotificationRepositoryMock()
        assert repo.delete_notification(32) == None

    def test_update_notification(self):
        repo = NotificationRepositoryMock()
        notification = repo.update_notification(repo.notifications[0].notification_id, "Maua Tech")

        assert notification.title == "Maua Tech"
        assert repo.notifications[0].title == "Maua Tech"

    def test_update_notification_not_found(self):
        repo = NotificationRepositoryMock()

        assert repo.update_notification(32, "Maua Tech") == None

