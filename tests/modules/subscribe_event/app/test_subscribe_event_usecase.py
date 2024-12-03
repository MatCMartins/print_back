from src.modules.subscribe_event.app.subscribe_event_usecase import SubscribeEventUsecase
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock

repo = EventRepositoryMock()

class Test_SubscribeEventUsecase:
    def test_subscribe_event_usecase(self):
        usecase = SubscribeEventUsecase(repo)

        event = usecase(repo.events[0].event_id, "7d644e62-ef8b-4728-a92b-becb8930c24e")
        
        assert event.rooms == {"Main Hall": 99, "Workshop Room 1": 30}