from src.modules.get_notification.app.get_notification_controller import GetNotificationController
from src.modules.get_notification.app.get_notification_usecase import GetNotificationUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.notification_repository_mock import NotificationRepositoryMock

repo = NotificationRepositoryMock()

class Test_GetNotificationController:
    def test_get_notification_controller(self):
        usecase = GetNotificationUsecase(repo)
        controller = GetNotificationController(usecase)

        request = HttpRequest(query_params={"notification_id": repo.notifications[0].notification_id})

        response = controller(request)

        assert response.status_code == 200
        assert response.body["title"] == repo.notifications[0].title
        assert response.body["description"] == repo.notifications[0].description
        assert response.body["creation_date"] == repo.notifications[0].creation_date
        assert response.body["has_seen"] == repo.notifications[0].has_seen

    def test_get_notification_controller_no_items_found(self):
        usecase = GetNotificationUsecase(repo)
        controller = GetNotificationController(usecase)

        request = HttpRequest(query_params={"notification_id": "12321"})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "No items found for Notification"
    
    def test_get_notification_controller_wrong_parameter_type(self):
        usecase = GetNotificationUsecase(repo)
        controller = GetNotificationController(usecase)

        request = HttpRequest(query_params={"notification_id": 1231})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field notification_id isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
        
    def test_get_notification_controller_missing_parameter(self):
        usecase = GetNotificationUsecase(repo)
        controller = GetNotificationController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field notification_id is missing"