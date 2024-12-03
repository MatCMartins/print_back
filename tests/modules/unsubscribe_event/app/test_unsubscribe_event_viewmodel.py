from src.modules.unsubscribe_event.app.unsubscribe_event_viewmodel import UnsubscribeEventViewmodel
from src.shared.domain.entities.event import Event
 

class Test_UnsubscribeEventViewmodel:
    def test_unsubcribe_event_viewmodel(self):
        event = Event(
            event_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            name="Tech Conference 2023",
            description="Annual tech conference for technology enthusiasts.",
            banner="https://techconf.com/banner.png",
            start_date=1672531200,
            end_date=1672617600,
            rooms={"Main Hall": 100, "Workshop Room 1": 30},
            subscribers={"user1": "Main Hall", "user2": "Workshop Room 1"}
        )

        viewmodel = UnsubscribeEventViewmodel(
            event_id=event.event_id,
            name=event.name,
            description=event.description,
            banner=event.banner,
            start_date=event.start_date,
            end_date=event.end_date,
            rooms=event.rooms,
            subscribers=event.subscribers
        )

        expected = {
            "event_id": "b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            "name": "Tech Conference 2023",
            "description": "Annual tech conference for technology enthusiasts.",
            "banner": "https://techconf.com/banner.png",
            "start_date": 1672531200,
            "end_date": 1672617600,
            "rooms": {"Main Hall": 100, "Workshop Room 1": 30},
            "subscribers": {"user1": "Main Hall", "user2": "Workshop Room 1"}
        }
        

        assert viewmodel.to_dict() == expected
()