from src.shared.domain.entities.event import Event
from src.shared.infra.dto.event_dynamo_dto import EventDynamoDTO
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock


class Test_EventDynamoDTO:
    def test_from_entity(self):
        repo = EventRepositoryMock()

        event_dto = EventDynamoDTO.from_entity(event=repo.events[0])

        expected_event_dto = EventDynamoDTO(
            event_id=repo.events[0].event_id,
            name=repo.events[0].name,
            description=repo.events[0].description,
            banner=repo.events[0].banner,
            start_date=repo.events[0].start_date,
            end_date=repo.events[0].end_date,
            rooms=repo.events[0].rooms,
            subscribers=repo.events[0].subscribers
        )

        assert event_dto == expected_event_dto

    def test_to_dynamo(self):
        repo = EventRepositoryMock()

        event_dto = EventDynamoDTO(
            event_id=repo.events[0].event_id,
            name=repo.events[0].name,
            description=repo.events[0].description,
            banner=repo.events[0].banner,
            start_date=repo.events[0].start_date,
            end_date=repo.events[0].end_date,
            rooms=repo.events[0].rooms,
            subscribers=repo.events[0].subscribers
        )

        event_dynamo = event_dto.to_dynamo()

        expected_dict = {
            "entity": "event",
            "event_id": repo.events[0].event_id,
            "name": repo.events[0].name,
            "description": repo.events[0].description,
            "banner": repo.events[0].banner,
            "start_date": repo.events[0].start_date,
            "end_date": repo.events[0].end_date,
            "rooms": repo.events[0].rooms,
            "subscribers": repo.events[0].subscribers
        }

        assert event_dynamo == expected_dict

    def test_from_dynamo(self):
        dynamo_dict = {
            'event_id': '1234',
            'name': 'Sample Event',
            'entity': 'event',
            'description': 'A sample event description',
            'banner': 'banner_url',
            'start_date': 123456790,
            'end_date': 123456791,
            'rooms': {'Room1': 50},
            'subscribers': {'user1': 'Room1'}
        }

        event_dto = EventDynamoDTO.from_dynamo(event_data=dynamo_dict)

        expected_event_dto = EventDynamoDTO(
            event_id='1234',
            name='Sample Event',
            description='A sample event description',
            banner='banner_url',
            start_date=123456790,
            end_date=123456791,
            rooms={'Room1': 50},
            subscribers={'user1': 'Room1'}
        )

        assert event_dto == expected_event_dto

    def test_to_entity(self):
        repo = EventRepositoryMock()

        event_dto = EventDynamoDTO(
            event_id=repo.events[0].event_id,
            name=repo.events[0].name,
            description=repo.events[0].description,
            banner=repo.events[0].banner,
            start_date=repo.events[0].start_date,
            end_date=repo.events[0].end_date,
            rooms=repo.events[0].rooms,
            subscribers=repo.events[0].subscribers
        )

        event_entity = event_dto.to_entity()

        assert event_entity.name == repo.events[0].name
        assert event_entity.description == repo.events[0].description
        assert event_entity.banner == repo.events[0].banner
        assert event_entity.start_date == repo.events[0].start_date
        assert event_entity.end_date == repo.events[0].end_date
        assert event_entity.rooms == repo.events[0].rooms
        assert event_entity.subscribers == repo.events[0].subscribers

    def test_from_dynamo_to_entity(self):
        dynamo_item = {
            'event_id': '1234',
            'name': 'Sample Event',
            'entity': 'event',
            'description': 'A sample event description',
            'banner': 'banner_url',
            'start_date': 123456790,
            'end_date': 123456791,
            'rooms': {'Room1': 50},
            'subscribers': {'user1': 'Room1'}
        }

        event_dto = EventDynamoDTO.from_dynamo(event_data=dynamo_item)
        event_entity = event_dto.to_entity()

        expected_event = Event(
            name='Sample Event',
            description='A sample event description',
            banner='banner_url',
            start_date=123456790,
            end_date=123456791,
            rooms={'Room1': 50},
            subscribers={'user1': 'Room1'}
        )

        assert event_entity.name == expected_event.name
        assert event_entity.description == expected_event.description
        assert event_entity.banner == expected_event.banner
        assert event_entity.start_date == expected_event.start_date
        assert event_entity.end_date == expected_event.end_date
        assert event_entity.rooms == expected_event.rooms
        assert event_entity.subscribers == expected_event.subscribers

    def test_from_entity_to_dynamo(self):
        repo = EventRepositoryMock()

        event_dto = EventDynamoDTO.from_entity(event=repo.events[0])
        event_dynamo = event_dto.to_dynamo()

        expected_dict = {
            "entity": "event",
            "event_id": repo.events[0].event_id,
            "name": repo.events[0].name,
            "description": repo.events[0].description,
            "banner": repo.events[0].banner,
            "start_date": repo.events[0].start_date,
            "end_date": repo.events[0].end_date,
            "rooms": repo.events[0].rooms,
            "subscribers": repo.events[0].subscribers
        }

        assert event_dynamo == expected_dict
