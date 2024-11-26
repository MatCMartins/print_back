import re
from src.modules.delete_course.app.delete_course_viewmodel import DeleteCourseViewmodel
from src.shared.domain.entities.course import Course


class Test_DeleteCourseViewmodel:
    def test_delete_course_viewmodel(self):
        course = Course(
            name="Computer Science",
            course_photo="https://example.com/computer_science_photo.jpg",
            coordinator="Alice Johnson",
            coordinator_photo="https://example.com/alice_photo.jpg",
            description="A course focused on programming, algorithms, and systems.",
            link="https://example.com/computer_science"
        )

        viewmodel = DeleteCourseViewmodel(
            course_id=course.course_id,
            name=course.name,
            course_photo=course.course_photo,
            coordinator=course.coordinator,
            coordinator_photo=course.coordinator_photo,
            description=course.description,
            link=course.link
        ).to_dict()

        assert re.match(r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$', viewmodel["course_id"])

        expected = {
            "course_id": course.course_id,
            "name": "Computer Science",
            "course_photo": "https://example.com/computer_science_photo.jpg",
            "coordinator": "Alice Johnson",
            "coordinator_photo": "https://example.com/alice_photo.jpg",
            "description": "A course focused on programming, algorithms, and systems.",
            "link": "https://example.com/computer_science"
        }	

        assert viewmodel == expected
