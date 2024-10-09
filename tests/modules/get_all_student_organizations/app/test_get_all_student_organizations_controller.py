from src.modules.get_all_student_organizations.app.get_all_student_organizations_controller import GetAllStudentOrganizationsController
from src.modules.get_all_student_organizations.app.get_all_student_organizations_usecase import GetAllStudentOrganizationsUsecase
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

repo = StudentOrganizationRepositoryMock()

class Test_GetAllStudentOrganizationsController:
    def test_get_all_student_organizations_controller(self):
        usecase = GetAllStudentOrganizationsUsecase(repo)
        controller = GetAllStudentOrganizationsController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request)

        assert response.status_code == 200