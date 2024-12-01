import os

import pytest

from src.shared.infra.repositories.notification_repository_dynamo import NotificationRepositoryDynamo
from src.shared.infra.repositories.notification_repository_mock import NotificationRepositoryMock
from src.shared.domain.entities.notification import Notification


class Test_NotificationRepositoryDynamo:

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_create_notification(self):

        notification_repository = NotificationRepositoryDynamo()
        notification_repository_mock = NotificationRepositoryMock()

        notification = Notification(
            title="Maua Tech Club", 
            description="A club for tech enthusiasts", 
            creation_date=1620009600, 
            has_seen=["7d644e62-ef8b-4728-a92b-becb8930c24e"]
        )

        resp = notification_repository.create_notification(notification)

        assert notification_repository_mock.notifications[0].title == resp.title

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_notification(self):

        notification_repository = NotificationRepositoryDynamo()
        notification_repository_mock = NotificationRepositoryMock()
        resp = notification_repository.get_notification(notification_repository_mock.notifications[0].notification_id)
        assert notification_repository_mock.notifications[0].title == resp.title

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_delete_notification(self):
        
        notification_repository = NotificationRepositoryDynamo()
        notification_repository_mock = NotificationRepositoryMock()
        resp = notification_repository.delete_notification(notification_repository_mock.notifications[1].notification_id)

        assert notification_repository_mock.notifications[1].title == resp.title

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_all_notifications(self):
        
        notification_repository = NotificationRepositoryDynamo()
        notification_repository_mock = NotificationRepositoryMock()
        resp = notification_repository.get_all_notifications()

        assert len(notification_repository_mock.notifications) == len(resp)

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_update_notification(self):
        
        notification_repository = NotificationRepositoryDynamo()
        notification_repository_mock = NotificationRepositoryMock()
        resp = notification_repository.update_notification(notification_id=notification_repository_mock.notifications[0].notification_id, new_title="Maua Tech")

        assert resp.title == "Maua Tech"