from src.shared.domain.entities.notification import Notification



class GetNotificationViewmodel:
    notification_id: str
    title: str
    description: str
    creation_date: str
    has_seen: list

    def __init__(self, notification_id: str, title: str, description: str, creation_date: str, has_seen: list):
        self.notification_id = notification_id
        self.title = title
        self.description = description
        self.creation_date = creation_date
        self.has_seen = has_seen
    
    def to_dict(self):
        return {
            "notification_id": self.notification_id,
            "title": self.title,
            "description": self.description,
            "creation_date": self.creation_date,
            "has_Seen": self.has_seen
        }
    
class GetAllNotificationsViewmodel:
    def __init__(self, notifications: list):
        self.notifications = notifications
    
    def to_dict(self):
        return {
            "notifications": [notification.to_dict() for notification in self.notifications]
        }
    