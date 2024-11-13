import re
from src.modules.delete_event.app.delete_event_controller import DeleteEventController
from src.modules.delete_event.app.delete_event_usecase import DeleteEventUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock

repo = EventRepositoryMock()

class Test_DeleteEventController:
    def test_delete_event_controller(self):
        usecase = DeleteEventUsecase(repo)
        controller = DeleteEventController(usecase)

        request = HttpRequest(query_params={"event_id": repo.events[0].event_id})

        response = controller(request)

        assert response.status_code == 200
        assert response.body["name"] == "Tech Conference 2023"
        assert response.body["description"] == "A conference for tech enthusiasts to discuss the latest trends in technology."
        assert response.body["banner"] == "https://techconference.com/banner.png"
        assert response.body["start_date"] == 1672531200
        assert response.body["end_date"] == 1672617600

    def test_delete_event_controller_no_items_found(self):
        usecase = DeleteEventUsecase(repo)
        controller = DeleteEventController(usecase)

        request = HttpRequest(query_params={"event_id": "nonexistent_id"})

        response = controller(request)
    
        assert response.status_code == 404
        assert response.body == "No items found for event_id"
    
    def test_delete_event_controller_wrong_parameter_type(self):
        usecase = DeleteEventUsecase(repo)
        controller = DeleteEventController(usecase)

        request = HttpRequest(query_params={"event_id": 1231})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field event_id isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
        
    def test_delete_event_controller_missing_parameter(self):
        usecase = DeleteEventUsecase(repo)
        controller = DeleteEventController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field event_id is missing"
    
    def test_delete_event_controller_uuid_format(self):
        # Check if the event_id follows UUIDv4 format
        event_id = repo.events[0].event_id
        uuid4_regex = r"^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$"
        
        assert re.match(uuid4_regex, event_id), f"event_id {event_id} is not a valid UUIDv4 format"
