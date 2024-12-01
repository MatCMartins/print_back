from uuid import uuid4
from src.shared.domain.repositories.notification_repository_interface import INotificationRepository
from src.shared.domain.entities.notification import Notification

class CreateNotificationUsecase:

    def __init__(self, repo: INotificationRepository):
        self.repo = repo
    def __call__(self, title: str, description: str, creation_date: str, has_seen: list):

        notification_id = str(uuid4())
        
        new_org = Notification(
            notification_id=notification_id,
            title=title,
            description=description,
            creation_date=creation_date,
            has_seen=has_seen
        )
        
        return self.repo.create_notification(new_org)