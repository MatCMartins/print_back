from src.modules.get_all_notifications.app.get_all_notifications_controller import GetAllNotificationsController
from src.modules.get_all_notifications.app.get_all_notifications_usecase import GetAllNotificationsUsecase
from src.shared.infra.repositories.notification_repository_mock import NotificationRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

repo = NotificationRepositoryMock()

class Test_GetAllNotificationsController:
    def test_get_all_notifications_controller(self):
        usecase = GetAllNotificationsUsecase(repo)
        controller = GetAllNotificationsController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request)

        assert response.status_code == 200