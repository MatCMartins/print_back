import re
from src.modules.create_course.app.create_course_viewmodel import CreateCourseViewModel
from src.shared.domain.entities.course import Course

class Test_CreateCourseViewmodel:
    def test_create_course_viewmodel(self):
        course = Course(
            course_id = "b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            name="Enactus IMT",
            description="Enactus IMT is a student organization that aims to develop projects that help the community.",
            course_photo="https://enactusimt.com/logo.png",
            coordinator="John Doe",
            coordinator_photo="https://enactusimt.com/coordinator.png",
            link="https://enactusimt.com"
        )


        viewmodel = CreateCourseViewModel(
            course_id=course.course_id,
            name=course.name,
            description=course.description,
            course_photo=course.course_photo,
            coordinator=course.coordinator,
            coordinator_photo=course.coordinator_photo,
            link=course.link
        )

        assert re.match(r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$', viewmodel.to_dict()["course_id"])

        expected = {
            "course_id": course.course_id,
            "name": "Enactus IMT",
            "description": "Enactus IMT is a student organization that aims to develop projects that help the community.",
            "course_photo": "https://enactusimt.com/logo.png",
            "coordinator": "John Doe",
            "coordinator_photo": "https://enactusimt.com/coordinator.png",
            "link": "https://enactusimt.com"
        }	

        assert viewmodel.to_dict() == expected