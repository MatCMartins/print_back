from src.modules.update_notification.app.update_notification_controller import UpdateNotificationController
from src.modules.update_notification.app.update_notification_usecase import UpdateNotificationUsecase
from src.shared.infra.repositories.notification_repository_mock import NotificationRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class Test_UpdateNotificationController:
    def test_update_notification_controller(self):
        repo = NotificationRepositoryMock()
        usecase = UpdateNotificationUsecase(repo)
        controller = UpdateNotificationController(usecase)

        response = HttpRequest(query_params={
            "notification_id": repo.notifications[0].notification_id,
            "title": "Maua Jr",
            "description": "This student organization is a junior company",
            "creation_date": 234567890,
            "has_seen": ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
        })

        response = controller(response)

        assert response.status_code == 200
        assert repo.notifications[0].title == "Maua Jr"
        assert repo.notifications[0].description == "This student organization is a junior company"
        assert repo.notifications[0].creation_date == 234567890
        assert repo.notifications[0].has_seen == ["7d644e62-ef8b-4728-a92b-becb8930c24e"]
    
    def test_update_notification_no_notification_id(self):
        repo = NotificationRepositoryMock()
        usecase = UpdateNotificationUsecase(repo)
        controller = UpdateNotificationController(usecase)

        response = HttpRequest(query_params={
            "title": "Maua Jr",
            "description": "This student organization is a junior company",
            "creation_date": 234567890,
            "has_seen": ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field notification_id is missing"
    
    def test_update_notification_wrong_title_type(self):
        repo = NotificationRepositoryMock()
        usecase = UpdateNotificationUsecase(repo)
        controller = UpdateNotificationController(usecase)

        response = HttpRequest(query_params={
            "notification_id": repo.notifications[0].notification_id,
            "title": 123,
            "description": "This student organization is a junior company",
            "creation_date": 234567890,
            "has_seen": ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field title isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
    
    def test_update_notification_wrong_description_type(self):
        repo = NotificationRepositoryMock()
        usecase = UpdateNotificationUsecase(repo)
        controller = UpdateNotificationController(usecase)

        response = HttpRequest(query_params={
            "notification_id": repo.notifications[0].notification_id,
            "title": "Maua Jr",
            "description": 123,
            "creation_date": 234567890,
            "has_seen": ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field description isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"

    def test_update_notification_wrong_creation_date_type(self):
        repo = NotificationRepositoryMock()
        usecase = UpdateNotificationUsecase(repo)
        controller = UpdateNotificationController(usecase)

        response = HttpRequest(query_params={
            "notification_id": repo.notifications[0].notification_id,
            "title": "Maua Jr",
            "description": "This student organization is a junior company",
            "creation_date": "234567890",
            "has_seen": ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field creation_date isn't the right type.\n Received: <class 'str'>.\n Expected: <class 'int'>"
    
    def test_update_notification_wrong_has_seen_type(self):
        repo = NotificationRepositoryMock()
        usecase = UpdateNotificationUsecase(repo)
        controller = UpdateNotificationController(usecase)

        response = HttpRequest(query_params={
            "notification_id": repo.notifications[0].notification_id,
            "title": "Maua Jr",
            "description": "This student organization is a junior company",
            "creation_date": 234567890,
            "has_seen": "b9799d9d-798c-4f44-9fd7-b9ae41c77496"
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field has_seen isn't the right type.\n Received: <class 'str'>.\n Expected: <class 'list'>"
    
 