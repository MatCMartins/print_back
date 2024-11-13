from src.shared.domain.entities.event import Event
from src.shared.domain.repositories.event_repository_interface import IEventRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class GetEventUsecase:

    def __init__(self, repo: IEventRepository):
        self.repo = repo
    
    def __call__(self, event_id: str) -> Event:
        event = self.repo.get_event(event_id)
        
        if not event:
            raise NoItemsFound("Event")
        
        return event
