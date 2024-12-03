from typing import List, Optional
from src.shared.domain.entities.event import Event
from src.shared.domain.repositories.event_repository_interface import IEventRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class EventRepositoryMock(IEventRepository):
    events: List[Event]

    def __init__(self):
        self.events = [
            Event(
                event_id="7d644e62-ef8b-4728-a92b-becb8930c24e",
                name="Tech Conference 2023",
                description="A conference for tech enthusiasts to discuss the latest trends in technology.",
                banner="https://techconference.com/banner.png",
                start_date=1672531200,
                end_date=1672617600,
                rooms={"Main Hall": 100, "Workshop Room 1": 30},
                subscribers={"user1": "Main Hall", "user2": "Workshop Room 1"}
            ),
            Event(
                event_id="7d644e62-ef8b-4728-a92b-becb8930c24e",
                name="AI Symposium",
                description="An event focused on advancements and applications in artificial intelligence.",
                banner="https://aisymposium.com/banner.png",
                start_date=1672704000,
                end_date=1672790400,
                rooms={"Auditorium": 200, "Lab 1": 50},
                subscribers={"user3": "Auditorium", "user4": "Lab 1"}
            ),
            Event(
                event_id="7d644e62-ef8b-4728-a92b-becb8930c24e",
                name="Robotics Competition",
                description="Annual competition for robotics teams from various universities.",
                banner="https://roboticscompetition.com/banner.png",
                start_date=1672876800,
                end_date=1672963200,
                rooms={"Arena": 150, "Workshop Area": 40},
                subscribers={"user5": "Arena", "user6": "Workshop Area"}
            )
        ]

    def get_event(self, event_id: str) -> Event:
        for event in self.events:
            if event.event_id == event_id:
                return event
        raise NoItemsFound("event_id")

    def get_all_events(self) -> List[Event]:
        return self.events

    def create_event(self, new_event: Event) -> Event:
        self.events.append(new_event)
        return new_event

    def delete_event(self, event_id: str) -> Event:
        for idx, event in enumerate(self.events):
            if event.event_id == event_id:
                return self.events.pop(idx)
        raise NoItemsFound("event_id")

    def update_event(self, event_id: str, new_name: Optional[str] = None, new_description: Optional[str] = None, new_banner: Optional[str] = None, new_start_date: Optional[int] = None, new_end_date: Optional[int] = None, new_rooms: Optional[dict] = None, new_subscribers: Optional[dict] = None) -> Event:
        for event in self.events:
            if event.event_id == event_id:
                if new_name is not None:
                    event.name = new_name
                if new_description is not None:
                    event.description = new_description
                if new_banner is not None:
                    event.banner = new_banner
                if new_start_date is not None:
                    event.start_date = new_start_date
                if new_end_date is not None:
                    event.end_date = new_end_date
                if new_rooms is not None:
                    event.rooms = new_rooms
                if new_subscribers is not None:
                    event.subscribers = new_subscribers
                return event
        raise NoItemsFound("event_id")
    
    def subscribe_event(self, event_id: str, member_id: str) -> Event:
        for event in self.events:
            if event.event_id == event_id:
                if sum(event.rooms.values()) > 0:
                    biggest_room = ""
                    for room in event.rooms.keys():
                        if biggest_room == "":
                            biggest_room = room
                        elif event.rooms[room] > event.rooms[biggest_room]:
                            biggest_room = room
                    event.rooms[biggest_room] -= 1
                    event.subscribers[member_id] = biggest_room
                return event
        raise NoItemsFound("event_id")
            
    def unsubscribe_event(self, event_id: str, member_id: str) -> Event:
        for event in self.events:
            if event.event_id == event_id:
                subscriber_room = event.subscribers[member_id]
                event.rooms[subscriber_room] += 1
                event.subscribers.pop(member_id)
                return event
        raise NoItemsFound("event_id")
                
                    

