from src.modules.get_all_events.app.get_all_events_viewmodel import GetAllEventsViewModel
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock

class Test_GetAllEventsViewModel:
    def test_get_all_events_viewmodel(self):
        events = EventRepositoryMock().events
        viewmodel = GetAllEventsViewModel(events).to_dict()
        
        expected = {
            "events": [
                {
                    "event_id": events[0].event_id,
                    "name": "Tech Conference 2023",
                    "description": "A conference for tech enthusiasts to discuss the latest trends in technology.",
                    "banner": "https://techconference.com/banner.png",
                    "start_date": 1672531200,
                    "end_date": 1672617600,
                    "rooms": {"Main Hall": 100, "Workshop Room 1": 30},
                    "subscribers": {"user1": "Main Hall", "user2": "Workshop Room 1"}
                },
                {
                    "event_id": events[1].event_id,
                    "name": "AI Symposium",
                    "description": "An event focused on advancements and applications in artificial intelligence.",
                    "banner": "https://aisymposium.com/banner.png",
                    "start_date": 1672704000,
                    "end_date": 1672790400,
                    "rooms": {"Auditorium": 200, "Lab 1": 50},
                    "subscribers": {"user3": "Auditorium", "user4": "Lab 1"}
                },
                {
                    "event_id": events[2].event_id,
                    "name": "Robotics Competition",
                    "description": "Annual competition for robotics teams from various universities.",
                    "banner": "https://roboticscompetition.com/banner.png",
                    "start_date": 1672876800,
                    "end_date": 1672963200,
                    "rooms": {"Arena": 150, "Workshop Area": 40},
                    "subscribers": {"user5": "Arena", "user6": "Workshop Area"}
                }
            ]
        }

        assert viewmodel == expected
