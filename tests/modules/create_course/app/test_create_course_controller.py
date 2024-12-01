from src.modules.create_course.app.create_course_controller import CreateCourseController
from src.modules.create_course.app.create_course_usecase import CreateCourseUsecase
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

repo = CourseRepositoryMock()

class Test_CreateCourseController:
    def test_create_course_controller(self):
        usecase = CreateCourseUsecase(repo)
        controller = CreateCourseController(usecase)

        request = HttpRequest(query_params={
            "course_id": "b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            "name": "Physics",
            "description": "A course focused on physics.",
            "course_photo": "https://example.com/physics_photo.jpg",
            "coordinator": "John Doe",
            "coordinator_photo": "https://example.com/john_photo.jpg",
            "link": "https://example.com/physics"
        })

        response = controller(request)

        assert response.status_code == 201
        assert response.body["name"] == "Physics"
        assert response.body["description"] == "A course focused on physics."
        assert response.body["course_photo"] == "https://example.com/physics_photo.jpg"
        assert response.body["coordinator"] == "John Doe"
        assert response.body["coordinator_photo"] == "https://example.com/john_photo.jpg"
        assert response.body["link"] == "https://example.com/physics"
    
    def test_create_course_controller_misssing_name(self):
        usecase = CreateCourseUsecase(repo)
        controller = CreateCourseController(usecase)

        request = HttpRequest(query_params={
            "description": "A course focused on physics.",
            "course_photo": "https://example.com/physics_photo.jpg",
            "coordinator": "John Doe",
            "coordinator_photo": "https://example.com/john_photo.jpg",
            "link": "https://example.com/physics"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field name is missing"
    
    def test_create_course_controller_misssing_description(self):
        usecase = CreateCourseUsecase(repo)
        controller = CreateCourseController(usecase)

        request = HttpRequest(query_params={
            "name": "Physics",
            "course_photo": "https://example.com/physics_photo.jpg",
            "coordinator": "John Doe",
            "coordinator_photo": "https://example.com/john_photo.jpg",
            "link": "https://example.com/physics"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field description is missing"
    
    def test_create_course_controller_misssing_course_photo(self):
        usecase = CreateCourseUsecase(repo)
        controller = CreateCourseController(usecase)

        request = HttpRequest(query_params={
            "name": "Physics",
            "description": "A course focused on physics.",
            "coordinator": "John Doe",
            "coordinator_photo": "https://example.com/john_photo.jpg",
            "link": "https://example.com/physics"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field course_photo is missing"

    def test_create_course_controller_misssing_coordinator(self):
        usecase = CreateCourseUsecase(repo)
        controller = CreateCourseController(usecase)

        request = HttpRequest(query_params={
            "name": "Physics",
            "description": "A course focused on physics.",
            "course_photo": "https://example.com/physics_photo.jpg",
            "coordinator_photo": "https://example.com/john_photo.jpg",
            "link": "https://example.com/physics"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field coordinator is missing"

    def test_create_course_controller_misssing_coordinator_photo(self):
        usecase = CreateCourseUsecase(repo)
        controller = CreateCourseController(usecase)

        request = HttpRequest(query_params={
            "name": "Physics",
            "description": "A course focused on physics.",
            "course_photo": "https://example.com/physics_photo.jpg",
            "coordinator": "John Doe",
            "link": "https://example.com/physics"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field coordinator_photo is missing"
    
    def test_create_course_controller_misssing_link(self):
        usecase = CreateCourseUsecase(repo)
        controller = CreateCourseController(usecase)

        request = HttpRequest(query_params={
            "name": "Physics",
            "description": "A course focused on physics.",
            "course_photo": "https://example.com/physics_photo.jpg",
            "coordinator": "John Doe",
            "coordinator_photo": "https://example.com/john_photo.jpg"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field link is missing"