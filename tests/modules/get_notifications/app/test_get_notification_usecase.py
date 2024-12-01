from src.modules.get_notification.app.get_notification_usecase import GetNotificationUsecase
from src.shared.infra.repositories.notification_repository_mock import NotificationRepositoryMock

repo = NotificationRepositoryMock()

class Test_GetNotificationUsecase:
    def test_get_notification_usecase(self):
        usecase = GetNotificationUsecase(repo)

        notification = usecase(repo.notifications[0].notification_id)

        assert notification.notification_id == repo.notifications[0].notification_id
        assert notification.title == repo.notifications[0].title
        assert notification.description == repo.notifications[0].description
        assert notification.creation_date == repo.notifications[0].creation_date
        assert notification.has_seen == repo.notifications[0].has_seen