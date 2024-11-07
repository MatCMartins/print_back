from src.modules.get_course.app.get_course_viewmodel import GetCourseViewmodel
from src.shared.domain.entities.course import Course


class Test_GetCourseViewmodel:
    def test_get_course_viewmodel(self):
        course = Course(
            name="name",
            course_photo="photo",
            coordinator="coordinator",
            coordinator_photo="photo",
            description="description",
            link="link"
        )

        viewmodel = GetCourseViewmodel(
            course_id=course.course_id,
            name=course.name,
            course_photo=course.course_photo,
            coordinator=course.coordinator,
            coordinator_photo=course.coordinator_photo,
            description=course.description,
            link=course.link
        ).to_dict()

        expected = {
            "course_id": course.course_id,
            "name": course.name,
            "course_photo": course.course_photo,
            "coordinator": course.coordinator,
            "coordinator_photo": course.coordinator_photo,
            "description": course.description,
            "link": course.link
        }	

        assert viewmodel == expected
