from src.modules.subscribe_event.app.subscribe_event_controller import SubscribeEventController
from src.modules.subscribe_event.app.subscribe_event_usecase import SubscribeEventUsecase
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

repo = EventRepositoryMock()

class Test_SubscribeEventsController:
    def test_subscribe_event_controller(self):
        usecase = SubscribeEventUsecase(repo)
        controller = SubscribeEventController(usecase)

        request = HttpRequest(query_params={
            "event_id": repo.events[0].event_id,
            "member_id": "7d644e62-ef8b-4728-a92b-becb8930c24e"
        })

        response = controller(request)

        assert response.status_code == 200