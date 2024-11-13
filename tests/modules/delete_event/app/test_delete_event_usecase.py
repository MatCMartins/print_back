import pytest
from src.modules.delete_event.app.delete_event_usecase import DeleteEventUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock

repo = EventRepositoryMock()

class Test_DeleteEventUsecase:
    def test_delete_event_usecase(self):
        usecase = DeleteEventUsecase(repo)
        deleted_event = usecase(repo.events[0].event_id)
        assert len(repo.events) == 2
        assert repo.events[0].name == "AI Symposium"
        assert repo.events[1].name == "Robotics Competition"
        assert deleted_event.name == "Tech Conference 2023"

    def test_delete_event_no_event_id(self):
        usecase = DeleteEventUsecase(repo)

        with pytest.raises(NoItemsFound):
            usecase("nonexistent_id")
