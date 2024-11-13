from src.modules.get_all_events.app.get_all_events_controller import GetAllEventsController
from src.modules.get_all_events.app.get_all_events_usecase import GetAllEventsUsecase
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

repo = EventRepositoryMock()

class Test_GetAllEventsController:
    def test_get_all_events_controller(self):
        usecase = GetAllEventsUsecase(repo)
        controller = GetAllEventsController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request)

        assert response.status_code == 200
        assert isinstance(response.body, dict)
        assert "events" in response.body
        events = response.body["events"]

        assert isinstance(events, list)
        assert len(events) == len(repo.events)

        for i, event in enumerate(events):
            assert event["name"] == repo.events[i].name
            assert event["description"] == repo.events[i].description
            assert event["banner"] == repo.events[i].banner
            assert event["start_date"] == repo.events[i].start_date
            assert event["end_date"] == repo.events[i].end_date
            assert event["rooms"] == repo.events[i].rooms
            assert event["subscribers"] == repo.events[i].subscribers
