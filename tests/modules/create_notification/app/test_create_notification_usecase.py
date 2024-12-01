from src.modules.create_notification.app.create_notification_usecase import CreateNotificationUsecase
from src.shared.infra.repositories.notification_repository_mock import NotificationRepositoryMock
from src.shared.domain.entities.notification import Notification

repo = NotificationRepositoryMock()

class Test_CreateNotificationUsecase:
    def test_create_notification_usecase(self):
        title = "EcoMauá"
        description = "The EcoMauá is a student organization that aims to promote sustainability and environmental awareness"
        creation_date = 234567890
        has_seen = ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]

        usecase = CreateNotificationUsecase(repo)
        response = usecase(title, description, creation_date, has_seen)

        assert response.title == title
        assert response.description == description
        assert response.creation_date == creation_date
        assert response.has_seen == has_seen
    
