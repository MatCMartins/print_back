import re
from src.modules.update_course.app.update_course_viewmodel import  UpdateCourseViewmodel
from src.shared.domain.entities.course import Course


class Test_UpdateCourseViewmodel:
    def test_update_course_viewmodel(self):
        course = Course(
            course_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            name="Computer Science",
            course_photo="https://example.com/computer_science_photo.jpg",
            coordinator="Alice Johnson",
            coordinator_photo="https://example.com/alice_photo.jpg",
            description="A course focused on programming, algorithms, and systems.",
            link="https://example.com/computer_science"
        )

        viewmodel = UpdateCourseViewmodel(
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
