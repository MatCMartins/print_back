import pytest
from src.modules.update_course.app.update_course_usecase import UpdateCourseUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock

class Test_UpdateCourseUsecase:
    def test_update_course_usecase(self):
        repo = CourseRepositoryMock()
        usecase = UpdateCourseUsecase(repo)
        first_course_id = repo.courses[0].course_id

        name="Mathematics"
        course_photo="photo"
        coordinator="coordinator"
        coordinator_photo="photo"
        description="description"
        link="link"

        response = usecase(
            course_id=first_course_id,
            name=name,
            course_photo=course_photo,
            coordinator=coordinator,
            coordinator_photo=coordinator_photo,
            description=description,
            link=link
        )

        assert response.course_id == first_course_id
        assert response.name == name
        assert response.course_photo == course_photo
        assert response.coordinator == coordinator
        assert response.coordinator_photo == coordinator_photo
        assert response.description == description
        assert response.link == link
    
    def test_update_course_no_stu_org_id(self):
        repo = CourseRepositoryMock()
        usecase = UpdateCourseUsecase(repo)

        name="Mathematics"
        course_photo="photo"
        coordinator="coordinator"
        coordinator_photo="photo"
        description="description"
        link="link"

  
        with pytest.raises(NoItemsFound):
            response = usecase(
                course_id="12321",
                name=name,
                course_photo=course_photo,
                coordinator=coordinator,
                coordinator_photo=coordinator_photo,
                description=description,
                link=link
        )
