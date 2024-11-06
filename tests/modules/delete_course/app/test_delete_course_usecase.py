import pytest
from src.modules.delete_course.app.delete_course_usecase import DeleteCourseUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock

repo = CourseRepositoryMock()

class Test_DeleteCourseUsecase:
    def test_delete_course_usecase(self):
        usecase = DeleteCourseUsecase(repo)

        stu_org = usecase(repo.courses[0].course_id)

        assert len(repo.courses) == 2
    
    def test_delete_course_no_stu_org_id(self):
        usecase = DeleteCourseUsecase(repo)

        with pytest.raises(NoItemsFound):
            response = usecase(None)
