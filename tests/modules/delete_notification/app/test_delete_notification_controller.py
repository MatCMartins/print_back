from src.modules.delete_notification.app.delete_notification_controller import DeleteNotificationController
from src.modules.delete_notification.app.delete_notification_usecase import DeleteNotificationsUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.notification_repository_mock import NotificationRepositoryMock

repo = NotificationRepositoryMock()

class Test_deleteNotificationController:
    def test_delete_notification_controller(self):
        usecase = DeleteNotificationsUsecase(repo)
        controller = DeleteNotificationController(usecase)

        request = HttpRequest(query_params={"notification_id": repo.notifications[0].notification_id})

        response = controller(request)

        assert response.status_code == 200
        assert repo.notifications[0].title == "AI Lab Mauá"
        assert repo.notifications[0].description == "A community focused on artificial intelligence research and applications, encouraging students to participate in AI projects."
        assert repo.notifications[0].creation_date == 1609459200
        assert repo.notifications[0].has_seen == ["7d644e62-ef8b-4728-a92b-becb8930c24e"]

    def test_delete_notification_controller_no_items_found(self):
        usecase = DeleteNotificationsUsecase(repo)
        controller = DeleteNotificationController(usecase)

        request = HttpRequest(query_params={"notification_id": "12321"})

        response = controller(request)
    
        assert response.status_code == 400
        assert response.body == "No items found for Notification"
    
    def test_delete_notification_controller_wrong_parameter_type(self):
        usecase = DeleteNotificationsUsecase(repo)
        controller = DeleteNotificationController(usecase)

        request = HttpRequest(query_params={"notification_id": 1231})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field notification_id isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
        
    def test_delete_notification_controller_missing_parameter(self):
        usecase = DeleteNotificationsUsecase(repo)
        controller = DeleteNotificationController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field notification_id is missing"