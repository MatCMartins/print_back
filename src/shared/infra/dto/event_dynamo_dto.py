from decimal import Decimal
from src.shared.domain.entities.event import Event
from typing import Optional, Dict


class EventDynamoDTO:
    event_id: str
    name: str
    description: str
    banner: Optional[str]
    start_date: int
    end_date: int
    rooms: Dict[str, int]
    subscribers: Dict[str, str]

    def __init__(self, event_id: str, name: str, description: str, banner: Optional[str], start_date: int, end_date: int, rooms: Dict[str, int], subscribers: Dict[str, str]):
        self.event_id = event_id
        self.name = name
        self.description = description
        self.banner = banner
        self.start_date = start_date
        self.end_date = end_date
        self.rooms = rooms
        self.subscribers = subscribers

    @staticmethod
    def from_entity(event: Event) -> "EventDynamoDTO":
        """
        Parse data from Event to EventDynamoDTO
        """
        return EventDynamoDTO(
            event_id=event.event_id,
            name=event.name,
            description=event.description,
            banner=event.banner,
            start_date=event.start_date,
            end_date=event.end_date,
            rooms=event.rooms,
            subscribers=event.subscribers
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from EventDynamoDTO to dict
        """
        return {
            "entity": "event",
            "event_id": self.event_id,
            "name": self.name,
            "description": self.description,
            "banner": self.banner,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "rooms": {k: str(v) for k,v in self.rooms.items()},
            "subscribers": self.subscribers
        }

    @staticmethod
    def from_dynamo(event_data: dict) -> "EventDynamoDTO":
        """
        Parse data from DynamoDB to EventDynamoDTO
        @param event_data: dict from DynamoDB
        """
        return EventDynamoDTO(
            event_id=event_data["event_id"],
            name=event_data["name"],
            description=event_data["description"],
            banner=event_data.get("banner"),
            start_date=int(event_data["start_date"]),
            end_date=int(event_data["end_date"]),
            rooms={k: int(v) for k,v in event_data["rooms"].items()},
            subscribers=event_data["subscribers"]
        )

    def to_entity(self) -> Event:
        """
        Parse data from EventDynamoDTO to Event
        """
        return Event(
            event_id=self.event_id,
            name=self.name,
            description=self.description,
            banner=self.banner,
            start_date=self.start_date,
            end_date=self.end_date,
            rooms=self.rooms,
            subscribers=self.subscribers
        )

    def __repr__(self):
        return f"EventDynamoDTO(event_id={self.event_id}, name={self.name}, description={self.description}, banner={self.banner}, start_date={self.start_date}, end_date={self.end_date}, rooms={self.rooms}, subscribers={self.subscribers})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
