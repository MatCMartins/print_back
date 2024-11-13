import pytest
from src.modules.update_event.app.update_event_usecase import UpdateEventUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock
from src.shared.domain.entities.event import Event

class Test_UpdateEventUsecase:
    def test_update_event_usecase(self):
        repo = EventRepositoryMock()
        usecase = UpdateEventUsecase(repo)
        first_event_id = repo.events[0].event_id

        name = "Tech Summit 2023"
        description = "Updated description for the annual tech summit."
        banner = "new_banner_url"
        start_date = 234567890
        end_date = 234567999
        rooms = {"Main Hall": 150}
        subscribers = {"user1": "Main Hall"}

        response = usecase(
            event_id=first_event_id,
            name=name,
            description=description,
            banner=banner,
            start_date=start_date,
            end_date=end_date,
            rooms=rooms,
            subscribers=subscribers
        )
        
        assert repo.events[0].name == "Tech Summit 2023"
        assert repo.events[0].description == "Updated description for the annual tech summit."
        assert repo.events[0].banner == "new_banner_url"
        assert repo.events[0].start_date == 234567890
        assert repo.events[0].end_date == 234567999
        assert repo.events[0].rooms == {"Main Hall": 150}
        assert repo.events[0].subscribers == {"user1": "Main Hall"}

    def test_update_event_no_event_id(self):
        repo = EventRepositoryMock()
        usecase = UpdateEventUsecase(repo)

        name = "Tech Summit 2023"
        description = "Updated description for the annual tech summit."
        banner = "new_banner_url"
        start_date = 234567890
        end_date = 234567999
        rooms = {"Main Hall": 150}
        subscribers = {"user1": "Main Hall"}

        with pytest.raises(NoItemsFound):
            usecase(
                event_id=None,
                name=name,
                description=description,
                banner=banner,
                start_date=start_date,
                end_date=end_date,
                rooms=rooms,
                subscribers=subscribers
            )
