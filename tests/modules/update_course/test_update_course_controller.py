from src.modules.update_course.app.update_course_controller import UpdateCourseController
from src.modules.update_course.app.update_course_usecase import UpdateCourseUsecase
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class Test_UpdateCourseController:
    def test_update_course_controller(self):
        repo = CourseRepositoryMock()
        usecase = UpdateCourseUsecase(repo)
        controller = UpdateCourseController(usecase)

        response = HttpRequest(query_params={
            "course_id": repo.courses[0].course_id,
            "name": "Mathematics",
            "course_photo": "photo",
            "coordinator": "coordinator",
            "coordinator_photo": "photo",
            "description": "description",
            "link": "link"
        })

        response = controller(response)

        assert response.status_code == 200
        assert response.body["course_id"] == repo.courses[0].course_id
        assert response.body["name"] == "Mathematics"
        assert response.body["course_photo"] == "photo"
        assert response.body["coordinator"] == "coordinator"
        assert response.body["coordinator_photo"] == "photo"
        assert response.body["description"] == "description"
        assert response.body["link"] == "link"
    
    def test_update_course_no_course_id(self):
        repo = CourseRepositoryMock()
        usecase = UpdateCourseUsecase(repo)
        controller = UpdateCourseController(usecase)

        response = HttpRequest(query_params={
            "name": "Maua Jr",
            "description": "This student organization is a junior company",
            "creation_date": 234567890,
            "logo": "logo",
            "instagram": "instagram",
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field course_id is missing"
    
    def test_update_course_wrong_name_type(self):
        repo = CourseRepositoryMock()
        usecase = UpdateCourseUsecase(repo)
        controller = UpdateCourseController(usecase)

        response = HttpRequest(query_params={
            "course_id": repo.courses[0].course_id,
            "name": 123,
            "course_photo": "photo",
            "coordinator": "coordinator",
            "coordinator_photo": "photo",
            "description": "description",
            "link": "link"
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field name isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
    
    def test_update_course_wrong_course_photo_type(self):
        repo = CourseRepositoryMock()
        usecase = UpdateCourseUsecase(repo)
        controller = UpdateCourseController(usecase)

        response = HttpRequest(query_params={
            "course_id": repo.courses[0].course_id,
            "name": "Mathematics",
            "course_photo": 123,
            "coordinator": "coordinator",
            "coordinator_photo": "photo",
            "description": "description",
            "link": "link"
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field course_photo isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
    
    def test_update_course_wrong_coordinator_type(self):
        repo = CourseRepositoryMock()
        usecase = UpdateCourseUsecase(repo)
        controller = UpdateCourseController(usecase)

        response = HttpRequest(query_params={
            "course_id": repo.courses[0].course_id,
            "name": "Mathematics",
            "course_photo": "photo",
            "coordinator": 123,
            "coordinator_photo": "photo",
            "description": "description",
            "link": "link"
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field coordinator isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
    
    def test_update_course_wrong_coordinator_photo_type(self):
        repo = CourseRepositoryMock()
        usecase = UpdateCourseUsecase(repo)
        controller = UpdateCourseController(usecase)

        response = HttpRequest(query_params={
            "course_id": repo.courses[0].course_id,
            "name": "Mathematics",
            "course_photo": "photo",
            "coordinator": "coordinator",
            "coordinator_photo": 123,
            "description": "description",
            "link": "link"
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field coordinator_photo isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
    
    def test_update_course_wrong_description_type(self):
        repo = CourseRepositoryMock()
        usecase = UpdateCourseUsecase(repo)
        controller = UpdateCourseController(usecase)

        response = HttpRequest(query_params={
            "course_id": repo.courses[0].course_id,
            "name": "Mathematics",
            "course_photo": "photo",
            "coordinator": "coordinator",
            "coordinator_photo": "photo",
            "description": 123,
            "link": "link"
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field description isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
    
    def test_update_course_wrong_link_type(self):
        repo = CourseRepositoryMock()
        usecase = UpdateCourseUsecase(repo)
        controller = UpdateCourseController(usecase)

        response = HttpRequest(query_params={
            "course_id": repo.courses[0].course_id,
            "name": "Mathematics",
            "course_photo": "photo",
            "coordinator": "coordinator",
            "coordinator_photo": "photo",
            "description": "description",
            "link": 123
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field link isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
    
    def test_update_course_no_items_found(self):
        repo = CourseRepositoryMock()
        usecase = UpdateCourseUsecase(repo)
        controller = UpdateCourseController(usecase)

        response = HttpRequest(query_params={
            "course_id": "12321",
            "name": "Mathematics",
            "course_photo": "photo",
            "coordinator": "coordinator",
            "coordinator_photo": "photo",
            "description": "description",
            "link": "link"
        })

        response = controller(response)

        assert response.status_code == 404
        assert response.body == "No items found for course_id"