from src.modules.get_all_courses.app.get_all_courses_usecase import GetAllCoursesUsecase
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock

repo = CourseRepositoryMock()

class Test_GetAllCoursesUsecase:
    def test_get_all_courses_usecase(self):
        usecase = GetAllCoursesUsecase(repo)

        course = usecase()
        
        assert len(course) == 3
        assert course[0].name == "Computer Science"
        assert course[1].name == "Data Analytics"
        assert course[2].name == "Marketing"