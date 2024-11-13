from src.modules.get_all_events.app.get_all_events_usecase import GetAllEventsUsecase
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock

repo = EventRepositoryMock()

class Test_GetAllEventsUsecase:
    def test_get_all_events_usecase(self):
        usecase = GetAllEventsUsecase(repo)

        events = usecase()
        
        assert len(events) == 3
        assert events[0].name == "Tech Conference 2023"
        assert events[1].name == "AI Symposium"
        assert events[2].name == "Robotics Competition"
