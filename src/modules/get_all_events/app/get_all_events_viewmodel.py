from src.shared.domain.entities.event import Event

class GetEventViewModel:
    event_id: str
    name: str
    description: str
    banner: str
    start_date: int
    end_date: int
    rooms: dict
    subscribers: dict

    def __init__(self, event_id: str, name: str, description: str, banner: str, start_date: int, end_date: int, rooms: dict, subscribers: dict):
        self.event_id = event_id
        self.name = name
        self.description = description
        self.banner = banner
        self.start_date = start_date
        self.end_date = end_date
        self.rooms = rooms
        self.subscribers = subscribers
    
    def to_dict(self):
        return {
            "event_id": self.event_id,
            "name": self.name,
            "description": self.description,
            "banner": self.banner,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rooms": self.rooms,
            "subscribers": self.subscribers
        }

class GetAllEventsViewModel:
    def __init__(self, events: list[Event]):
        self.events = [GetEventViewModel(
            event_id=event.event_id,
            name=event.name,
            description=event.description,
            banner=event.banner,
            start_date=event.start_date,
            end_date=event.end_date,
            rooms=event.rooms,
            subscribers=event.subscribers
        ) for event in events]
    
    def to_dict(self):
        return {
            "events": [event.to_dict() for event in self.events]
        }
