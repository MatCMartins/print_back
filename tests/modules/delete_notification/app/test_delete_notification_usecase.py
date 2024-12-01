import pytest
from src.modules.delete_notification.app.delete_notification_usecase import DeleteNotificationsUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.notification_repository_mock import NotificationRepositoryMock

repo = NotificationRepositoryMock()

class Test_DeleteNotificationUsecase:
    def test_delete_notification_usecase(self):
        usecase = DeleteNotificationsUsecase(repo)

        notification = usecase(repo.notifications[0].notification_id)

        assert len(repo.notifications) == 2
        assert repo.notifications[0].title == "AI Lab Mauá"
        assert repo.notifications[1].title == "Robotics Team Mauá"
    
    def test_delete_notification_no_notification_id(self):
        usecase = DeleteNotificationsUsecase(repo)

        with pytest.raises(NoItemsFound):
            response = usecase(None)
