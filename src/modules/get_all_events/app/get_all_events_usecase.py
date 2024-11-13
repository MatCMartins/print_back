from src.shared.domain.entities.event import Event
from src.shared.domain.repositories.event_repository_interface import IEventRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class GetAllEventsUsecase:

    def __init__(self, repo: IEventRepository):
        self.repo = repo
    
    def __call__(self) -> list[Event]:
        events = self.repo.get_all_events()
        
        if len(events) == 0:
            raise NoItemsFound("events")
        
        return events
