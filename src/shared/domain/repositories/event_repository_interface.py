from abc import ABC, abstractmethod
from typing import List, Optional

from src.shared.domain.entities.event import Event


class IEventRepository(ABC):

    @abstractmethod
    def get_event(self, event_id: str) -> Event:
        """
        If event_id not found, raise NoItemsFound
        """
        pass

    @abstractmethod
    def get_all_events(self) -> List[Event]:
        pass

    @abstractmethod
    def create_event(self, new_event: Event) -> Event:
        pass

    @abstractmethod
    def delete_event(self, event_id: str) -> Event:
        """
        If event_id not found, raise NoItemsFound
        """
        pass

    @abstractmethod
    def update_event(self, event_id: str, new_name: Optional[str] = None, new_description: Optional[str] = None, new_banner: Optional[str] = None, new_start_date: Optional[int] = None, new_end_date: Optional[int] = None, new_rooms: Optional[dict] = None, new_subscribers: Optional[dict] = None) -> Event:
        """
        If event_id not found, raise NoItemsFound
        """
        pass

    @abstractmethod
    def subscribe_event(self, event_id: str, member_id: str) -> Event:
        """
        If event_id not found, raise NoItemsFound
        """
        pass

    @abstractmethod
    def unsubscribe_event(self, event_id: str, member_id: str) -> Event:
        """
        If event_id not found, raise NoItemsFound
        """
        pass
