from abc import ABC, abstractmethod
from typing import List, Optional

from src.shared.domain.entities.notification import Notification


class INotifocationRepository(ABC):

    @abstractmethod
    def get_notification(self, notification_id: str) -> Notification:
        """
        If notification_id not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def get_all_notifications(self) -> List[Notification]:
        pass

    @abstractmethod
    def create_notification(self, new_notification: Notification) -> Notification:
        pass

    @abstractmethod
    def delete_notification(self, notification_id: str) -> Notification:
        """
        If notification_id not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def update_notification(self, notification_id: str, new_title: Optional[str] = None, new_description: Optional[str] = None, new_creation_date: int = None, new_has_seen: Optional[list] = None) -> Notification:
        """
        If notification_id not found raise NoItemsFound
        """
        pass
