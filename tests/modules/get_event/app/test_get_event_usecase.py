from src.modules.get_event.app.get_event_usecase import GetEventUsecase
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound
import pytest

repo = EventRepositoryMock()

class Test_GetEventUsecase:
    def test_get_event_usecase(self):
        usecase = GetEventUsecase(repo)

        event = usecase(repo.events[0].event_id)

        assert event.event_id == repo.events[0].event_id
        assert event.name == repo.events[0].name
        assert event.description == repo.events[0].description
        assert event.banner == repo.events[0].banner
        assert event.start_date == repo.events[0].start_date
        assert event.end_date == repo.events[0].end_date
        assert event.rooms == repo.events[0].rooms
        assert event.subscribers == repo.events[0].subscribers

    def test_get_event_usecase_no_items_found(self):
        usecase = GetEventUsecase(repo)

        with pytest.raises(NoItemsFound):
            usecase("nonexistent_id")
