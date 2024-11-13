from src.modules.create_event.app.create_event_controller import CreateEventController
from src.modules.create_event.app.create_event_usecase import CreateEventUsecase
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

repo = EventRepositoryMock()

class Test_CreateEventController:
    def test_create_event_controller(self):
        usecase = CreateEventUsecase(repo)
        controller = CreateEventController(usecase)

        request = HttpRequest(query_params={
            "name": "Tech Conference 2023",
            "description": "Annual tech conference",
            "banner": "banner_url",
            "start_date": 1672531200,
            "end_date": 1672617600,
            "rooms": {"Main Hall": 100, "Workshop Room 1": 30},
            "subscribers": {"user1": "Main Hall", "user2": "Workshop Room 1"}
        })

        response = controller(request)

        assert response.status_code == 201
        assert response.body["name"] == "Tech Conference 2023"
        assert response.body["description"] == "Annual tech conference"
        assert response.body["banner"] == "banner_url"
        assert response.body["start_date"] == 1672531200
        assert response.body["end_date"] == 1672617600
        assert response.body["rooms"] == {"Main Hall": 100, "Workshop Room 1": 30}
        assert response.body["subscribers"] == {"user1": "Main Hall", "user2": "Workshop Room 1"}
    
    def test_create_event_controller_missing_name(self):
        usecase = CreateEventUsecase(repo)
        controller = CreateEventController(usecase)

        request = HttpRequest(query_params={
            "description": "Annual tech conference",
            "banner": "banner_url",
            "start_date": 1672531200,
            "end_date": 1672617600,
            "rooms": {"Main Hall": 100, "Workshop Room 1": 30},
            "subscribers": {"user1": "Main Hall", "user2": "Workshop Room 1"}
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field name is missing"
    
    def test_create_event_controller_missing_description(self):
        usecase = CreateEventUsecase(repo)
        controller = CreateEventController(usecase)

        request = HttpRequest(query_params={
            "name": "Tech Conference 2023",
            "banner": "banner_url",
            "start_date": 1672531200,
            "end_date": 1672617600,
            "rooms": {"Main Hall": 100, "Workshop Room 1": 30},
            "subscribers": {"user1": "Main Hall", "user2": "Workshop Room 1"}
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field description is missing"
    
    def test_create_event_controller_missing_banner(self):
        usecase = CreateEventUsecase(repo)
        controller = CreateEventController(usecase)

        request = HttpRequest(query_params={
            "name": "Tech Conference 2023",
            "description": "Annual tech conference",
            "start_date": 1672531200,
            "end_date": 1672617600,
            "rooms": {"Main Hall": 100, "Workshop Room 1": 30},
            "subscribers": {"user1": "Main Hall", "user2": "Workshop Room 1"}
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field banner is missing"
    
    def test_create_event_controller_missing_start_date(self):
        usecase = CreateEventUsecase(repo)
        controller = CreateEventController(usecase)

        request = HttpRequest(query_params={
            "name": "Tech Conference 2023",
            "description": "Annual tech conference",
            "banner": "banner_url",
            "end_date": 1672617600,
            "rooms": {"Main Hall": 100, "Workshop Room 1": 30},
            "subscribers": {"user1": "Main Hall", "user2": "Workshop Room 1"}
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field start_date is missing"

    def test_create_event_controller_missing_end_date(self):
        usecase = CreateEventUsecase(repo)
        controller = CreateEventController(usecase)

        request = HttpRequest(query_params={
            "name": "Tech Conference 2023",
            "description": "Annual tech conference",
            "banner": "banner_url",
            "start_date": 1672531200,
            "rooms": {"Main Hall": 100, "Workshop Room 1": 30},
            "subscribers": {"user1": "Main Hall", "user2": "Workshop Room 1"}
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field end_date is missing"
    
    def test_create_event_controller_missing_rooms(self):
        usecase = CreateEventUsecase(repo)
        controller = CreateEventController(usecase)

        request = HttpRequest(query_params={
            "name": "Tech Conference 2023",
            "description": "Annual tech conference",
            "banner": "banner_url",
            "start_date": 1672531200,
            "end_date": 1672617600,
            "subscribers": {"user1": "Main Hall", "user2": "Workshop Room 1"}
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field rooms is missing"
    
    def test_create_event_controller_missing_subscribers(self):
        usecase = CreateEventUsecase(repo)
        controller = CreateEventController(usecase)

        request = HttpRequest(query_params={
            "name": "Tech Conference 2023",
            "description": "Annual tech conference",
            "banner": "banner_url",
            "start_date": 1672531200,
            "end_date": 1672617600,
            "rooms": {"Main Hall": 100, "Workshop Room 1": 30}
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field subscribers is missing"
