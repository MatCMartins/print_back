from src.modules.create_course.app.create_course_usecase import CreateCourseUsecase
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock
from src.shared.domain.entities.course import Course

repo = CourseRepositoryMock()

class Test_CreateCourseUsecase:
    def test_create_course_usecase(self):
        name = "Physics"
        description = "A course focused on physics."
        course_photo = "https://example.com/physics_photo.jpg"
        coordinator = "John Doe"
        coordinator_photo = "https://example.com/john_photo.jpg"
        link = "https://example.com/physics"

        usecase = CreateCourseUsecase(repo)
        response = usecase(name, course_photo, coordinator, coordinator_photo, description, link)

        assert response.name == name
        assert response.description == description
        assert response.course_photo == course_photo
        assert response.coordinator == coordinator
        assert response.coordinator_photo == coordinator_photo
        assert response.link == link
            
    
