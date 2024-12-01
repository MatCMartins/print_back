from src.modules.create_notification.app.create_notification_controller import CreateNotificationController
from src.modules.create_notification.app.create_notification_usecase import CreateNotificationUsecase
from src.shared.infra.repositories.notification_repository_mock import NotificationRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

repo = NotificationRepositoryMock()

class Test_CreateNotificationController:
    def test_create_notification_controller(self):
        usecase = CreateNotificationUsecase(repo)
        controller = CreateNotificationController(usecase)

        request = HttpRequest(query_params={
            "title": "Data Science Club IMT",
            "description": "Data Science Club IMT",
            "creation_date": 234567890,
            "has_seen": ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
        })

        response = controller(request)

        assert response.status_code == 201
        assert response.body["title"] == "Data Science Club IMT"
        assert response.body["description"] == "Data Science Club IMT"
        assert response.body["creation_date"] == 234567890
        assert response.body["has_seen"] == ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
    
    def test_create_notification_controller_misssing_title(self):
        usecase = CreateNotificationUsecase(repo)
        controller = CreateNotificationController(usecase)

        request = HttpRequest(query_params={
            "description": "Data Science Club IMT",
            "creation_date": 234567890,
            "has_seen": ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field title is missing"
    
    def test_create_notification_controller_misssing_description(self):
        usecase = CreateNotificationUsecase(repo)
        controller = CreateNotificationController(usecase)

        request = HttpRequest(query_params={
            "title": "Data Science Club IMT",
            "creation_date": 234567890,
            "has_seen": ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field description is missing"
    
    def test_create_notification_controller_misssing_creation_date(self):
        usecase = CreateNotificationUsecase(repo)
        controller = CreateNotificationController(usecase)

        request = HttpRequest(query_params={
            "title": "Data Science Club IMT",
            "description": "Data Science Club IMT",
            "has_seen": ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field creation_date is missing"
    

    def test_create_notification_controller_misssing_has_seen(self):
        usecase = CreateNotificationUsecase(repo)
        controller = CreateNotificationController(usecase)

        request = HttpRequest(query_params={
            "title": "Data Science Club IMT",
            "description": "Data Science Club IMT",
            "creation_date": 234567890,
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field has_seen is missing"
    