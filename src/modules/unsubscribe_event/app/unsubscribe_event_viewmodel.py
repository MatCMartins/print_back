from typing import Optional, Dict

class UnsubscribeEventViewmodel:
    event_id: str
    name: str
    description: str
    banner: Optional[str]
    start_date: int
    end_date: int
    rooms: Dict[str, int]
    subscribers: Dict[str, str]

    def __init__(self, event_id: str, name: str, description: str, banner: Optional[str], start_date: int, end_date: int, rooms : Dict[str, int], subscribers : Dict[str, str]):
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
            "subscribers": self.subscribers,
            
        }
    