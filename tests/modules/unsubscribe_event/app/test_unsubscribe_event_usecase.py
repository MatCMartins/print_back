from src.modules.unsubscribe_event.app.unsubscribe_event_usecase import UnsubscribeEventUsecase
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock

repo = EventRepositoryMock()

class Test_UnsubscribeEventUsecase:
    def test_unsubscribe_event_usecase(self):
        usecase = UnsubscribeEventUsecase(repo)

        event = usecase(repo.events[0].event_id, "user1")
        
        assert event.rooms == {"Main Hall": 101, "Workshop Room 1": 30}