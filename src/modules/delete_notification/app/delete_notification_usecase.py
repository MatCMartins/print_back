from src.shared.domain.entities.notification import Notification
from src.shared.domain.repositories.notification_repository_interface import INotificationRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound



class DeleteNotificationsUsecase:

    def __init__(self, repo: INotificationRepository):
        self.repo = repo
    
    def __call__(self, notification_id: str):

        if not self.repo.get_notification(notification_id):
            raise NoItemsFound("Notification")
        
        return self.repo.delete_notification(notification_id)
