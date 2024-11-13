from src.modules.update_event.app.update_event_controller import UpdateEventController
from src.modules.update_event.app.update_event_usecase import UpdateEventUsecase
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class Test_UpdateEventController:
    def test_update_event_controller(self):
        repo = EventRepositoryMock()
        usecase = UpdateEventUsecase(repo)
        controller = UpdateEventController(usecase)

        request = HttpRequest(query_params={
            "event_id": repo.events[0].event_id,
            "name": "Tech Summit 2023",
            "description": "Annual tech summit event.",
            "banner": "new_banner_url",
            "start_date": 234567890,
            "end_date": 234567999,
            "rooms": {"Conference Hall": 200},
            "subscribers": {"user1": "Conference Hall"}
        })

        response = controller(request)

        assert response.status_code == 200
        assert repo.events[0].name == "Tech Summit 2023"
        assert repo.events[0].description == "Annual tech summit event."
        assert repo.events[0].banner == "new_banner_url"
        assert repo.events[0].start_date == 234567890
        assert repo.events[0].end_date == 234567999
        assert repo.events[0].rooms == {"Conference Hall": 200}
        assert repo.events[0].subscribers == {"user1": "Conference Hall"}

    def test_update_event_no_event_id(self):
        repo = EventRepositoryMock()
        usecase = UpdateEventUsecase(repo)
        controller = UpdateEventController(usecase)

        request = HttpRequest(query_params={
            "name": "Tech Summit 2023",
            "description": "Annual tech summit event.",
            "banner": "new_banner_url",
            "start_date": 234567890,
            "end_date": 234567999
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field event_id is missing"

    def test_update_event_wrong_name_type(self):
        repo = EventRepositoryMock()
        usecase = UpdateEventUsecase(repo)
        controller = UpdateEventController(usecase)

        request = HttpRequest(query_params={
            "event_id": repo.events[0].event_id,
            "name": 123,
            "description": "Annual tech summit event.",
            "banner": "new_banner_url",
            "start_date": 234567890,
            "end_date": 234567999
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field name isn't the right type.\n Received: int.\n Expected: str"

    def test_update_event_wrong_start_date_type(self):
        repo = EventRepositoryMock()
        usecase = UpdateEventUsecase(repo)
        controller = UpdateEventController(usecase)

        request = HttpRequest(query_params={
            "event_id": repo.events[0].event_id,
            "name": "Tech Summit 2023",
            "description": "Annual tech summit event.",
            "banner": "new_banner_url",
            "start_date": "234567890",
            "end_date": 234567999
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field start_date isn't the right type.\n Received: str.\n Expected: int"

    def test_update_event_wrong_rooms_type(self):
        repo = EventRepositoryMock()
        usecase = UpdateEventUsecase(repo)
        controller = UpdateEventController(usecase)

        request = HttpRequest(query_params={
            "event_id": repo.events[0].event_id,
            "name": "Tech Summit 2023",
            "description": "Annual tech summit event.",
            "banner": "new_banner_url",
            "start_date": 234567890,
            "end_date": 234567999,
            "rooms": "Conference Hall",
            "subscribers": {"user1": "Conference Hall"}
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field rooms isn't the right type.\n Received: str.\n Expected: dict"
