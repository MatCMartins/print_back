from src.modules.unsubscribe_event.app.unsubscribe_event_controller import UnsubscribeEventController
from src.modules.unsubscribe_event.app.unsubscribe_event_usecase import UnsubscribeEventUsecase
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

repo = EventRepositoryMock()

class Test_UnsubscribeEventsController:
    def test_unsubscribe_event_controller(self):
        usecase = UnsubscribeEventUsecase(repo)
        controller = UnsubscribeEventController(usecase)

        request = HttpRequest(query_params={
            "event_id": repo.events[0].event_id,
            "member_id": "user1"
        })

        response = controller(request)

        assert response.status_code == 200