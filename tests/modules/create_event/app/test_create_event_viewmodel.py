import uuid
import re
from src.modules.create_event.app.create_event_viewmodel import CreateEventViewModel
from src.shared.domain.entities.event import Event

class Test_CreateEventViewModel:
    def test_create_event_viewmodel(self):
        event = Event(
            name="Tech Conference 2023",
            description="Annual tech conference for technology enthusiasts.",
            banner="https://techconf.com/banner.png",
            start_date=1672531200,
            end_date=1672617600,
            rooms={"Main Hall": 100, "Workshop Room 1": 30},
            subscribers={"user1": "Main Hall", "user2": "Workshop Room 1"}
        )

        viewmodel = CreateEventViewModel(
            event_id=event.event_id,
            name=event.name,
            description=event.description,
            banner=event.banner,
            start_date=event.start_date,
            end_date=event.end_date,
            rooms=event.rooms,
            subscribers=event.subscribers
        )

        # Verifica se o event_id gerado é um UUIDv4 válido
        assert re.match(r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$', viewmodel.to_dict()["event_id"])

        expected = {
            "name": "Tech Conference 2023",
            "description": "Annual tech conference for technology enthusiasts.",
            "banner": "https://techconf.com/banner.png",
            "start_date": 1672531200,
            "end_date": 1672617600,
            "rooms": {"Main Hall": 100, "Workshop Room 1": 30},
            "subscribers": {"user1": "Main Hall", "user2": "Workshop Room 1"}
        }

        # Removemos o `event_id` da verificação do expected, pois ele agora é um UUIDv4
        event_dict = viewmodel.to_dict()
        event_dict.pop("event_id")
        
        assert event_dict == expected
