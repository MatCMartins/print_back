from src.shared.domain.entities.event import Event
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock
import pytest


class Test_EventRepositoryMock:

    def test_get_event(self):
        repo = EventRepositoryMock()
        event = repo.get_event(repo.events[0].event_id)

        assert event.name == "Tech Conference 2023"
        assert event.banner == "https://techconference.com/banner.png"
        assert event.description == "A conference for tech enthusiasts to discuss the latest trends in technology."
        assert event.start_date == 1672531200
        assert event.end_date == 1672617600
        assert event.rooms == {"Main Hall": 100, "Workshop Room 1": 30}
        assert event.subscribers == {"user1": "Main Hall", "user2": "Workshop Room 1"}

    def test_get_event_not_found(self):
        repo = EventRepositoryMock()
        with pytest.raises(NoItemsFound):
            repo.get_event("nonexistent_id")
    
    def test_get_all_events(self):
        repo = EventRepositoryMock()
        events = repo.get_all_events()
        assert len(events) == 3

    def test_create_event(self):
        repo = EventRepositoryMock()
        event = Event(
            event_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            name="AI Summit",
            description="A summit on artificial intelligence advancements.",
            banner="https://aisummit.com/banner.png",
            start_date=1673000000,
            end_date=1673086400,
            rooms={"Main Hall": 150},
            subscribers={"user3": "Main Hall"}
        )

        repo.create_event(event)

        assert repo.events[3].name == "AI Summit"
        assert repo.events[3].description == "A summit on artificial intelligence advancements."
        assert repo.events[3].banner == "https://aisummit.com/banner.png"
        assert repo.events[3].start_date == 1673000000
        assert repo.events[3].end_date == 1673086400
        assert repo.events[3].rooms == {"Main Hall": 150}
        assert repo.events[3].subscribers == {"user3": "Main Hall"}
    
    def test_delete_event(self):
        repo = EventRepositoryMock()
        event = repo.delete_event(repo.events[0].event_id)

        assert event.name == "Tech Conference 2023"
        assert len(repo.events) == 2
    
    def test_delete_event_not_found(self):
        repo = EventRepositoryMock()
        with pytest.raises(NoItemsFound):
            repo.delete_event("nonexistent_id")
    
    def test_update_event(self):
        repo = EventRepositoryMock()
        event = repo.update_event(
            event_id=repo.events[0].event_id, 
            new_name="AI Summit",
            new_description="A summit on AI advancements.",
            new_banner="https://aisummit.com/banner.png",
            new_start_date=1673000000,
            new_end_date=1673086400,
            new_rooms={"Main Hall": 150},
            new_subscribers={"user3": "Main Hall"}
        )

        assert event.name == "AI Summit"
        assert repo.events[0].name == "AI Summit"
        assert repo.events[0].description == "A summit on AI advancements."
        assert repo.events[0].banner == "https://aisummit.com/banner.png"
        assert repo.events[0].start_date == 1673000000
        assert repo.events[0].end_date == 1673086400
        assert repo.events[0].rooms == {"Main Hall": 150}
        assert repo.events[0].subscribers == {"user3": "Main Hall"}
    
    def test_update_event_not_found(self):
        repo = EventRepositoryMock()
        with pytest.raises(NoItemsFound):
            repo.update_event("nonexistent_id", new_name="AI Summit")

    def test_update_event_name(self):
        repo = EventRepositoryMock()
        event = repo.update_event(repo.events[0].event_id, new_name="AI Summit")

        assert event.name == "AI Summit"
        assert repo.events[0].name == "AI Summit"
    
    def test_update_event_banner(self):
        repo = EventRepositoryMock()
        event = repo.update_event(repo.events[0].event_id, new_banner="https://newbanner.com/banner.png")

        assert repo.events[0].banner == "https://newbanner.com/banner.png"
    
    def test_subscribe_event(self):
        repo = EventRepositoryMock()
        event = repo.subscribe_event(repo.events[0].event_id, "7d644e62-ef8b-4728-a92b-becb8930c24e")

        assert event.subscribers == {"user1": "Main Hall", "user2": "Workshop Room 1", "7d644e62-ef8b-4728-a92b-becb8930c24e": "Main Hall"}
        assert repo.events[0].rooms == {"Main Hall": 99, "Workshop Room 1": 30}
        assert event.rooms == {"Main Hall": 99, "Workshop Room 1": 30}

    def test_subscribe_event_wrong_event_id(self):
        repo = EventRepositoryMock()

        with pytest.raises(NoItemsFound):
            repo.subscribe_event("nonexistent_id", "7d644e62-ef8b-4728-a92b-becb8930c24e")

    def test_unsubscribe_event(self):
        repo = EventRepositoryMock()
        event = repo.unsubscribe_event(repo.events[0].event_id, "user1")

        assert event.subscribers == {"user2": "Workshop Room 1"}
        assert repo.events[0].rooms == {"Main Hall": 101, "Workshop Room 1": 30}
        assert event.rooms == {"Main Hall": 101, "Workshop Room 1": 30}

    def test_unsubscribe_event_wrong_event_id(self):
        repo = EventRepositoryMock()

        with pytest.raises(NoItemsFound):
            repo.subscribe_event("nonexistent_id", "7d644e62-ef8b-4728-a92b-becb8930c24e")

