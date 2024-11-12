from src.modules.delete_course.app.delete_course_controller import DeleteCourseController
from src.modules.delete_course.app.delete_course_usecase import DeleteCourseUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock

repo = CourseRepositoryMock()

class Test_deleteCourseController:
    def test_delete_course_controller(self):
        usecase = DeleteCourseUsecase(repo)
        controller = DeleteCourseController(usecase)

        request = HttpRequest(query_params={"course_id": repo.courses[0].course_id})

        response = controller(request)

        assert response.status_code == 200
        assert response.body["name"] == "Computer Science"
        assert response.body["course_photo"] == "https://example.com/computer_science_photo.jpg"
        assert response.body["coordinator"] == "Alice Johnson"
        assert response.body["coordinator_photo"] == "https://example.com/alice_photo.jpg"
        assert response.body["description"] == "A course focused on programming, algorithms, and systems."
        assert response.body["link"] == "https://example.com/computer_science"

    def test_delete_course_controller_no_items_found(self):
        usecase = DeleteCourseUsecase(repo)
        controller = DeleteCourseController(usecase)

        request = HttpRequest(query_params={"course_id": "12321"})

        response = controller(request)
    
        assert response.status_code == 400
        assert response.body == "No items found for course_id"
    
    def test_delete_course_controller_wrong_parameter_type(self):
        usecase = DeleteCourseUsecase(repo)
        controller = DeleteCourseController(usecase)

        request = HttpRequest(query_params={"course_id": 1231})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field course_id isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
        
    def test_delete_course_controller_missing_parameter(self):
        usecase = DeleteCourseUsecase(repo)
        controller = DeleteCourseController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field course_id is missing"