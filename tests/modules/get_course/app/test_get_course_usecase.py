from src.modules.get_course.app.get_course_usecase import GetCourseUsecase
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock

repo = CourseRepositoryMock()

class Test_GetCourseUsecase:
    def test_get_course_usecase(self):
        usecase = GetCourseUsecase(repo)
        course = usecase(repo.courses[0].course_id)

        assert course.course_id == repo.courses[0].course_id
        assert course.name == repo.courses[0].name
        assert course.description == repo.courses[0].description
        assert course.coordinator == repo.courses[0].coordinator
        assert course.link == repo.courses[0].link
        assert course.course_photo == repo.courses[0].course_photo
        assert course.coordinator_photo == repo.courses[0].coordinator_photo