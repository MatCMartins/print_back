from src.modules.get_course.app.get_course_controller import GetCourseController
from src.modules.get_course.app.get_course_usecase import GetCourseUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock

repo = CourseRepositoryMock()

class Test_GetCourseController:
    def test_get_course_controller(self):
        usecase = GetCourseUsecase(repo)
        controller = GetCourseController(usecase)

        request = HttpRequest(query_params={"course_id": repo.courses[0].course_id})

        response = controller(request)

        assert response.status_code == 200
        assert response.body["name"] == repo.courses[0].name
        assert response.body["description"] == repo.courses[0].description
        assert response.body["coordinator"] == repo.courses[0].coordinator
        assert response.body["link"] == repo.courses[0].link
        assert response.body["course_photo"] == repo.courses[0].course_photo
        assert response.body["coordinator_photo"] == repo.courses[0].coordinator_photo
        

    def test_get_course_controller_no_items_found(self):
        usecase = GetCourseUsecase(repo)
        controller = GetCourseController(usecase)

        request = HttpRequest(query_params={"course_id": "12321"})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "No items found for course_id"
    
    def test_get_course_controller_wrong_parameter_type(self):
        usecase = GetCourseUsecase(repo)
        controller = GetCourseController(usecase)

        request = HttpRequest(query_params={"course_id": 1231})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field course_id isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
        
    def test_get_course_controller_missing_parameter(self):
        usecase = GetCourseUsecase(repo)
        controller = GetCourseController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field course_id is missing"