from src.modules.create_event.app.create_event_usecase import CreateEventUsecase
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock
from src.shared.domain.entities.event import Event

repo = EventRepositoryMock()

class Test_CreateEventUsecase:
    def test_create_event_usecase(self):
        name = "Tech Conference 2023"
        description = "Annual tech conference for technology enthusiasts"
        banner = "banner_url"
        start_date = 1672531200
        end_date = 1672617600
        rooms = {"Main Hall": 100, "Workshop Room 1": 30}
        subscribers = {"user1": "Main Hall", "user2": "Workshop Room 1"}

        usecase = CreateEventUsecase(repo)
        response = usecase(name, description, banner, start_date, end_date, rooms, subscribers)

        assert response.name == name
        assert response.description == description
        assert response.banner == banner
        assert response.start_date == start_date
        assert response.end_date == end_date
        assert response.rooms == rooms
        assert response.subscribers == subscribers
