from src.shared.domain.entities.event import Event
from src.shared.domain.repositories.event_repository_interface import IEventRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.usecase_errors import UserNotRegistered



class UnsubscribeEventUsecase:

    def __init__(self, repo: IEventRepository):
        self.repo = repo
    
    def __call__(self, event_id: str, member_id: str):
        event = self.repo.get_event(event_id)
        if not event:
            raise NoItemsFound("Event")
        if member_id not in event.subscribers.keys():
            raise UserNotRegistered("member_id")
        
        return self.repo.unsubscribe_event(event_id, member_id)
