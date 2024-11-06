from src.modules.get_student_organization.app.get_student_organization_usecase import GetStudentOrganizationUsecase
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock

repo = StudentOrganizationRepositoryMock()

class Test_GetStudentOrganizationUsecase:
    def test_get_student_organization_usecase(self):
        usecase = GetStudentOrganizationUsecase(repo)

        stu_org = usecase(repo.stu_orgs[0].stu_org_id)

        assert stu_org.stu_org_id == repo.stu_orgs[0].stu_org_id
        assert stu_org.name == repo.stu_orgs[0].name
        assert stu_org.description == repo.stu_orgs[0].description
        assert stu_org.creation_date == repo.stu_orgs[0].creation_date
        assert stu_org.logo == repo.stu_orgs[0].logo
        assert stu_org.instagram == repo.stu_orgs[0].instagram
        assert stu_org.website_link == repo.stu_orgs[0].website_link