from src.modules.get_all_courses.app.get_all_courses_controller import GetAllCoursesController
from src.modules.get_all_courses.app.get_all_courses_usecase import GetAllCoursesUsecase
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

repo = CourseRepositoryMock()

class Test_GetAllCoursesController:
    def test_get_all_courses_controller(self):
        usecase = GetAllCoursesUsecase(repo)
        controller = GetAllCoursesController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request)

        assert response.status_code == 200