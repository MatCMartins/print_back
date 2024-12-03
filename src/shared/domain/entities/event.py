import abc
from decimal import Decimal
import uuid
from typing import Optional, Dict
from src.shared.helpers.errors.domain_errors import EntityError

class Event(abc.ABC):
    event_id: str
    name: str
    description: str
    banner: Optional[str]
    start_date: int
    end_date: int
    rooms: Dict[str, int]
    subscribers: Dict[str, str]

    def __init__(self, event_id: str, name: str, description: str, banner: Optional[str], start_date: int, end_date: int, rooms: Dict[str, int], subscribers: Dict[str, str]):

        if not self.validate_string(name):
            raise EntityError("Field Invalid name")
        self.name = name

        if not self.validate_string(description):
            raise EntityError("Field Invalid description")
        self.description = description

        if banner is not None and not self.validate_string(banner):
            raise EntityError("Field Invalid banner")
        self.banner = banner

        if not self.validate_date(start_date):
            raise EntityError("Field Invalid start_date")
        self.start_date = start_date

        if not self.validate_date(end_date):
            raise EntityError("Field Invalid end_date")
        self.end_date = end_date

        if not self.validate_rooms(rooms):
            raise EntityError("Field Invalid rooms")
        self.rooms = rooms

        if not self.validate_subscribers(subscribers, rooms):
            raise EntityError("Field Invalid subscribers")
        self.subscribers = subscribers

        if not self.validate_id(event_id):
            raise EntityError("Field Invalid event_id")
        self.event_id = event_id

    @staticmethod
    def validate_string(param: str) -> bool:
        return param is not None and isinstance(param, str)

    @staticmethod
    def validate_date(param: int) -> bool:
        if param is None:
            return False
        if type(param) != int:
            return False
        return True
    
    @staticmethod
    def validate_id(id: str) -> bool:
        if id is None:
            return False
        elif type(id) != str:
            return False
        elif len(id) != 36:
            return False
        return True

    @staticmethod
    def validate_rooms(rooms: Dict[str, int]) -> bool:
        if not isinstance(rooms, dict):
            return False
        for room, capacity in rooms.items():
            if not isinstance(room, str) or not isinstance(capacity, int):
                return False
        return True

    @staticmethod
    def validate_subscribers(subscribers: Dict[str, str], rooms: Dict[str, int]) -> bool:
        if not isinstance(subscribers, dict):
            return False
        for subscriber_id, room_name in subscribers.items():
            if not isinstance(subscriber_id, str) or not isinstance(room_name, str):
                return False
            if room_name not in rooms:
                return False
        return True

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

    def __repr__(self):
        return f"Event(event_id={self.event_id}, name={self.name}, description={self.description}, banner={self.banner}, start_date={self.start_date}, end_date={self.end_date}, rooms={self.rooms}, subscribers={self.subscribers})"
