from src.modules.delete_event.app.delete_event_viewmodel import DeleteEventViewModel
from src.shared.domain.entities.event import Event

class Test_DeleteEventViewModel:
    def test_delete_event_viewmodel(self):
        event = Event(
            name="Tech Conference 2023",
            description="Annual tech conference for technology enthusiasts.",
            banner="https://techconf.com/banner.png",
            start_date=1672531200,
            end_date=1672617600,
            rooms={"Main Hall": 100, "Workshop Room 1": 30},
            subscribers={"user1": "Main Hall", "user2": "Workshop Room 1"}
        )

        viewmodel = DeleteEventViewModel(
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
