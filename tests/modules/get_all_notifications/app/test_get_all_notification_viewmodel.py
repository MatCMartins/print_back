from src.modules.get_all_notifications.app.get_all_notifications_viewmodel import GetAllNotificationsViewmodel
from src.shared.infra.repositories.notification_repository_mock import NotificationRepositoryMock
 

class Test_GetAllNotificationsViewmodel:
    def test_get_all_notifications_viewmodel(self):
        notifications = NotificationRepositoryMock().notifications
        viewmodel = GetAllNotificationsViewmodel(notifications).to_dict()
        expected = {"notifications":
            [
                {
                    "notification_id": notifications[0].notification_id,
                    "title": "Data Science Club IMT",
                    "description": "Organization dedicated to promoting knowledge and projects in the field of data science and machine learning.",
                    "creation_date": 1620009600,
                    "has_seen": ["7d644e62-ef8b-4728-a92b-becb8930c24e"]
                },
                {
                    "notification_id": notifications[1].notification_id,
                    "title": "AI Lab Mauá",
                    "description": "A community focused on artificial intelligence research and applications, encouraging students to participate in AI projects.",
                    "creation_date": 1609459200,
                    "has_seen": ["7d644e62-ef8b-4728-a92b-becb8930c24e"]
                },
                {
                    "notification_id": notifications[2].notification_id,
                    "title": "Robotics Team Mauá",
                    "description": "A student organization focused on building and programming autonomous robots to compete in national and international competitions.",
                    "creation_date": 1619827200,
                    "has_seen": ["7d644e62-ef8b-4728-a92b-becb8930c24e"]
                }
            ]
        }

        assert viewmodel == expected
