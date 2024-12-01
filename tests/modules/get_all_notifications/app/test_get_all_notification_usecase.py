from src.modules.get_all_notifications.app.get_all_notifications_usecase import GetAllNotificationsUsecase
from src.shared.infra.repositories.notification_repository_mock import NotificationRepositoryMock

repo = NotificationRepositoryMock()

class Test_GetAllNotificationsUsecase:
    def test_get_all_notifications_usecase(self):
        usecase = GetAllNotificationsUsecase(repo)

        notification = usecase()
        
        assert len(notification) == 3
        assert notification[0].title == "Data Science Club IMT"
        assert notification[1].title == "AI Lab Mauá"
        assert notification[2].title == "Robotics Team Mauá"