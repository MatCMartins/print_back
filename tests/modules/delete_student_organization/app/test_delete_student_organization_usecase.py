from src.modules.delete_student_organization.app.delete_student_organization_usecase import DeleteStudentOrganizationsUsecase
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock

repo = StudentOrganizationRepositoryMock()

class Test_DeleteStudentOrganizationUsecase:
    def test_delete_student_organization_usecase(self):
        usecase = DeleteStudentOrganizationsUsecase(repo)

        stu_org = usecase(repo.stu_orgs[0].stu_org_id)

        assert len(repo.stu_orgs) == 2
        assert repo.stu_orgs[0].name == "AI Lab Mauá"
        assert repo.stu_orgs[1].name == "Robotics Team Mauá"