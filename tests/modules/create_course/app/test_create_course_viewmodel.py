import hashlib
from src.modules.create_course.app.create_course_viewmodel import CreateCourseViewModel
from src.shared.domain.entities.course import Course

class Test_CreateCourseViewmodel:
    def test_create_course_viewmodel(self):
        course = Course(
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

        expected = {
            "course_id": hashlib.md5(("Enactus IMT").encode()).hexdigest(),
            "name": "Enactus IMT",
            "description": "Enactus IMT is a student organization that aims to develop projects that help the community.",
            "course_photo": "https://enactusimt.com/logo.png",
            "coordinator": "John Doe",
            "coordinator_photo": "https://enactusimt.com/coordinator.png",
            "link": "https://enactusimt.com"
        }	

        assert viewmodel.to_dict() == expected