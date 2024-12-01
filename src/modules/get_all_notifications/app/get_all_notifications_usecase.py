from src.shared.domain.entities.notification import Notification
from src.shared.domain.repositories.notification_repository_interface import INotificationRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound



class GetAllNotificationsUsecase:

    def __init__(self, repo: INotificationRepository):
        self.repo = repo
    
    def __call__(self) -> list[Notification]:
        notifications = self.repo.get_all_notifications()
        
        if len(notifications) == 0:
            raise NoItemsFound("notifications")
        
        return notifications
