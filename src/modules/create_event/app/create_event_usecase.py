from uuid import uuid4
from src.shared.domain.repositories.event_repository_interface import IEventRepository
from src.shared.domain.entities.event import Event

class CreateEventUsecase:

    def __init__(self, repo: IEventRepository):
        self.repo = repo

    def __call__(self, name: str, description: str, banner: str, start_date: int, end_date: int, rooms: dict, subscribers: dict):
        
        event_id = str(uuid4())

        new_event = Event(
            event_id=event_id,
            name=name,
            description=description,
            banner=banner,
            start_date=start_date,
            end_date=end_date,
            rooms=rooms,
            subscribers=subscribers
        )
        
        return self.repo.create_event(new_event)
