import abc
import uuid
from typing import Optional

from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError

class Notification(abc.ABC):
    notification_id: str
    title: str
    description: str
    creation_date: int
    has_seen: list

    def __init__(self, notification_id: str, title: str, description: str, creation_date: int, has_seen: list):

        if not self.validate_parameters(title):
            raise EntityError("Invalid Title")
        self.title = title
        
        if not self.validate_parameters(description):
            raise EntityError("Invalid description")
        self.description = description

        if not self.validate_creation_date(creation_date):
            raise EntityError("Invalid creation_date")
        self.creation_date = creation_date
        
        if not self.validate_creation_has_seen(has_seen):
            raise EntityError("Invalid has_seen")
        self.has_seen = has_seen

        if not self.validate_id(notification_id):
            raise EntityError("Invalid notification_id")
        self.notification_id = notification_id
        
    @staticmethod
    def validate_parameters(param: str) -> bool:
        if param is None:
            return False
        elif type(param) != str:
            return False
        return True

    @staticmethod
    def validate_creation_date(param: int) -> bool:
        if param is None:
            return False
        elif type(param) != int:
            return False
        return True
    
    @staticmethod
    def validate_creation_has_seen(param: list) -> bool:
        if param is None:
            return False
        elif type(param) != list:
            return False
        for p in param:
            if len(p) != 36:
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

    def to_dict(self):
        return {
            "notification_id": self.notification_id,
            "title": self.title,
            "description": self.description,
            "creation_date": self.creation_date,
            "has_seen": self.has_seen,
        }

    def __repr__(self):
        return f"Notification(notification_id={self.notification_id}, title={self.title}, description={self.description}, creation_date={self.creation_date} has_seen={self.has_seen})"
