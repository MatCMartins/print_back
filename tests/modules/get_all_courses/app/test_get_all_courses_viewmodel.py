from src.modules.get_all_courses.app.get_all_courses_viewmodel import GetAllCoursesViewmodel
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock
 

class Test_GetAllCoursesViewmodel:
    def test_get_all_courses_viewmodel(self):
        courses = CourseRepositoryMock().courses
        viewmodel = GetAllCoursesViewmodel(courses).to_dict()
        expected = {"courses":
            [
                {
                    "course_id": "8329f5105520a1b72d062628c077ddfa",
                    "name": "Computer Science",
                    "course_photo": "https://example.com/computer_science_photo.jpg",
                    "coordinator": "Alice Johnson",
                    "coordinator_photo": "https://example.com/alice_photo.jpg",
                    "description": "A course focused on programming, algorithms, and systems.",
                    "link": "https://example.com/computer_science"
                },
                {
                    "course_id": "e19e98a669ae21f94ffd1659998fd072",
                    "name": "Data Analytics",
                    "course_photo": "https://example.com/data_analytics_photo.jpg",
                    "coordinator": "Bob Smith",
                    "coordinator_photo": "https://example.com/bob_photo.jpg",
                    "description": "Learn how to analyze data and extract meaningful insights.",
                    "link": "https://example.com/data_analytics"
                },
                {
                    "course_id": "7cb15e416d62919b1b40298324fbe30b",
                    "name": "Marketing",
                    "course_photo": "https://example.com/marketing_photo.jpg",
                    "coordinator": "Carla Williams",
                    "coordinator_photo": "https://example.com/carla_photo.jpg",
                    "description": "Explore strategies for product promotion and brand management.",
                    "link": None
                }
            ]
        }

        assert viewmodel == expected
