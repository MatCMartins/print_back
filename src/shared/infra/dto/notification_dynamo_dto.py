
from src.shared.domain.entities.notification import Notification
from src.shared.domain.enums.state_enum import STATE


class NotificationDynamoDTO:
    notification_id: str
    title: str
    description: str
    creation_date: int
    has_seen: list

    def __init__(self, notification_id: str, title: str, description: str, creation_date: int, has_seen: list):
        self.notification_id = notification_id
        self.title = title
        self.description = description
        self.creation_date = creation_date
        self.has_seen = has_seen
    @staticmethod
    def from_entity(notification: Notification) -> "NotificationDynamoDTO":
        """
        Parse data from Notification to NotificationDynamoDTO
        """
        return NotificationDynamoDTO(
            notification_id=notification.notification_id,
            title=notification.title,
            description=notification.description,
            creation_date=notification.creation_date,
            has_seen=notification.has_seen
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from NotificationDynamoDTO to dict
        """
        return {
            "entity": "notification",
            "notification_id": self.notification_id,
            "title": self.title,
            "description": self.description,
            "creation_date": self.creation_date,
            "has_seen": self.has_seen
        }

    @staticmethod
    def from_dynamo(notification_data: dict) -> "NotificationDynamoDTO":
        """
        Parse data from DynamoDB to NotificationDynamoDTO
        @param notification_data: dict from DynamoDB
        """
        return NotificationDynamoDTO(
            notification_id=notification_data["notification_id"],
            title=notification_data["title"],
            description=notification_data["description"],
            creation_date=notification_data["creation_date"],
            has_seen=notification_data["has_seen"]
        )

    def to_entity(self) -> Notification:
        """
        Parse data from NotificationDynamoDTO to Notification
        """
        return Notification(
            notification_id=self.notification_id,
            title=self.title,
            description=self.description,
            creation_date=int(self.creation_date),
            has_seen=list(self.has_seen)
        )

    def __repr__(self):
        return f"NotificationDynamoDTO(notification_id={self.notification_id} title={self.title}, description={self.description}, creation_date={self.creation_date}, has_seen={self.has_seen})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
