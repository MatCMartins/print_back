import pytest

from src.shared.infra.repositories.event_repository_dynamo import EventRepositoryDynamo
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock
from src.shared.domain.entities.event import Event


class Test_EventRepositoryDynamo:

    @pytest.mark.skip(reason="Needs DynamoDB")
    def test_create_event(self):

        event_repository = EventRepositoryDynamo()
        event_repository_mock = EventRepositoryMock()

        event = Event(
            name="Tech Conference",
            description="A conference for discussing the latest trends in technology.",
            banner="https://techconference.com/banner.png",
            start_date=1672531200,
            end_date=1672617600,
            rooms={"Main Hall": 100},
            subscribers={"user1": "Main Hall"}
        )

        resp = event_repository.create_event(event)

        assert event_repository_mock.events[0].name == resp.name

    @pytest.mark.skip(reason="Needs DynamoDB")
    def test_get_event(self):

        event_repository = EventRepositoryDynamo()
        event_repository_mock = EventRepositoryMock()
        resp = event_repository.get_event(event_repository_mock.events[0].event_id)
        assert event_repository_mock.events[0].name == resp.name

    @pytest.mark.skip(reason="Needs DynamoDB")
    def test_delete_event(self):
        
        event_repository = EventRepositoryDynamo()
        event_repository_mock = EventRepositoryMock()
        resp = event_repository.delete_event(event_repository_mock.events[1].event_id)

        assert event_repository_mock.events[1].name == resp.name

    @pytest.mark.skip(reason="Needs DynamoDB")
    def test_get_all_events(self):
        
        event_repository = EventRepositoryDynamo()
        event_repository_mock = EventRepositoryMock()
        resp = event_repository.get_all_events()

        assert len(event_repository_mock.events) == len(resp)

    @pytest.mark.skip(reason="Needs DynamoDB")
    def test_update_event(self):
        
        event_repository = EventRepositoryDynamo()
        event_repository_mock = EventRepositoryMock()
        resp = event_repository.update_event(event_id=event_repository_mock.events[0].event_id, new_name="Tech Conference 2023")

        assert resp.name == "Tech Conference 2023"
    
    @pytest.mark.skip(reason="Needs DynamoDB")
    def test_subscribe_event(self):
        
        event_repository = EventRepositoryDynamo()
        event_repository_mock = EventRepositoryMock()
        resp = event_repository.subscribe_event(event_id=event_repository_mock.events[0].event_id, member_id="7d644e62-ef8b-4728-a92b-becb8930c24e")

        assert resp.subscribers == {"user1": "Main Hall", "user2": "Workshop Room 1", "7d644e62-ef8b-4728-a92b-becb8930c24e": "Main Hall"}
        assert resp.rooms == {"Main Hall": 99, "Workshop Room 1": 30}

    @pytest.mark.skip(reason="Needs DynamoDB")
    def test_unsubscribe_event(self):
        
        event_repository = EventRepositoryDynamo()
        event_repository_mock = EventRepositoryMock()
        resp = event_repository.subscribe_event(event_id=event_repository_mock.events[0].event_id, member_id="user1")

        assert resp.subscribers == {"user2": "Workshop Room 1"}
        assert resp.rooms == {"Main Hall": 101, "Workshop Room 1": 30}
    
    
