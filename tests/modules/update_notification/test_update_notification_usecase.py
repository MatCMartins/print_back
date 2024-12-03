import pytest
from src.modules.update_notification.app.update_notification_usecase import UpdateNotificationUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.notification_repository_mock import NotificationRepositoryMock
from src.shared.domain.entities.notification import Notification

class Test_UpdateNotificationUsecase:
    def test_update_notification_usecase(self):
        repo = NotificationRepositoryMock()
        usecase = UpdateNotificationUsecase(repo)
        first_notification_id = repo.notifications[0].notification_id

        title="Maua Jr"
        description="This student organization is a junior company"
        creation_date=234567890
        has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]

        response = usecase(
            notification_id=first_notification_id,
            title=title,
            description=description,
            creation_date=creation_date,
            has_seen=has_seen
        )
        
        assert repo.notifications[0].title == "Maua Jr"
        assert repo.notifications[0].description == "This student organization is a junior company"
        assert repo.notifications[0].creation_date == 234567890
        assert repo.notifications[0].has_seen == ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
    
    def test_update_notification_no_notification_id(self):
        repo = NotificationRepositoryMock()
        usecase = UpdateNotificationUsecase(repo)

        title="Maua Jr"
        description="This student organization is a junior company"
        creation_date=234567890
        has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]

  
        with pytest.raises(NoItemsFound):
            response = usecase(
            notification_id=None,
            title=title,
            description=description,
            creation_date=creation_date,
            has_seen=["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
        )
