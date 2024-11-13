from src.modules.update_event.app.update_event_viewmodel import UpdateEventViewModel
from src.shared.domain.entities.event import Event

class Test_UpdateEventViewModel:
    def test_update_event_viewmodel(self):
        event = Event(
            name="Tech Summit",
            description="An annual tech summit.",
            banner="https://techsummit.com/banner.png",
            start_date=1672531200,
            end_date=1672617600,
            rooms={"Main Hall": 150},
            subscribers={"user1": "Main Hall", "user2": "Main Hall"}
        )

        viewmodel = UpdateEventViewModel(
            event_id=event.event_id,
            name=event.name,
            description=event.description,
            banner=event.banner,
            start_date=event.start_date,
            end_date=event.end_date,
            rooms=event.rooms,
            subscribers=event.subscribers
        ).to_dict()

        expected = {
            "event_id": event.event_id,
            "name": event.name,
            "description": event.description,
            "banner": event.banner,
            "start_date": event.start_date,
            "end_date": event.end_date,
            "rooms": event.rooms,
            "subscribers": event.subscribers
        }

        assert viewmodel == expected
