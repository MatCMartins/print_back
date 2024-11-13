from typing import Optional
from src.shared.domain.entities.event import Event
from src.shared.domain.repositories.event_repository_interface import IEventRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class UpdateEventUsecase:

    def __init__(self, repo: IEventRepository):
        self.repo = repo
    
    def __call__(self, event_id: str, name: Optional[str] = None, description: Optional[str] = None, banner: Optional[str] = None, start_date: Optional[int] = None, end_date: Optional[int] = None, rooms: Optional[dict] = None, subscribers: Optional[dict] = None) -> Event:
        
        if not self.repo.get_event(event_id):
            raise NoItemsFound("Event")
        
        return self.repo.update_event(event_id, name, description, banner, start_date, end_date, rooms, subscribers)
