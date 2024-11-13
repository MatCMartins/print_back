from src.modules.get_event.app.get_event_controller import GetEventController
from src.modules.get_event.app.get_event_usecase import GetEventUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock

repo = EventRepositoryMock()

class Test_GetEventController:
    def test_get_event_controller(self):
        usecase = GetEventUsecase(repo)
        controller = GetEventController(usecase)

        request = HttpRequest(query_params={"event_id": repo.events[0].event_id})

        response = controller(request)

        assert response.status_code == 200
        assert response.body["name"] == repo.events[0].name
        assert response.body["description"] == repo.events[0].description
        assert response.body["banner"] == repo.events[0].banner
        assert response.body["start_date"] == repo.events[0].start_date
        assert response.body["end_date"] == repo.events[0].end_date
        assert response.body["rooms"] == repo.events[0].rooms
        assert response.body["subscribers"] == repo.events[0].subscribers

    def test_get_event_controller_no_items_found(self):
        usecase = GetEventUsecase(repo)
        controller = GetEventController(usecase)

        request = HttpRequest(query_params={"event_id": "nonexistent_id"})

        response = controller(request)

        assert response.status_code == 404
        assert response.body == "No items found for event_id"
    
    def test_get_event_controller_wrong_parameter_type(self):
        usecase = GetEventUsecase(repo)
        controller = GetEventController(usecase)

        request = HttpRequest(query_params={"event_id": 1231})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field event_id isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
        
    def test_get_event_controller_missing_parameter(self):
        usecase = GetEventUsecase(repo)
        controller = GetEventController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field event_id is missing"
