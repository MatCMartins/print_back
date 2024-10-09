from src.modules.get_student_organization.app.get_student_organization_controller import GetStudentOrganizationController
from src.modules.get_student_organization.app.get_student_organization_usecase import GetStudentOrganizationsUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock

repo = StudentOrganizationRepositoryMock()

class Test_StudentOrganizationController:
    def test_get_student_organization_controller(self):
        usecase = GetStudentOrganizationsUsecase(repo)
        controller = GetStudentOrganizationController(usecase)

        request = HttpRequest(query_params={"stu_org_id": repo.stu_orgs[0].stu_org_id})

        response = controller(request)

        assert response.status_code == 200
        assert response.body["name"] == repo.stu_orgs[0].name
        assert response.body["description"] == repo.stu_orgs[0].description
        assert response.body["creation_date"] == repo.stu_orgs[0].creation_date
        assert response.body["logo"] == repo.stu_orgs[0].logo
        assert response.body["instagram"] == repo.stu_orgs[0].instagram
        assert response.body["website_link"] == repo.stu_orgs[0].website_link
