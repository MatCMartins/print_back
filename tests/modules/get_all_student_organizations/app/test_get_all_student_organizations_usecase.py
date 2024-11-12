from src.modules.get_all_student_organizations.app.get_all_student_organizations_usecase import GetAllStudentOrganizationsUsecase
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock

repo = StudentOrganizationRepositoryMock()

class Test_GetAllStudentOrganizationsUsecase:
    def test_get_all_student_organizations_usecase(self):
        usecase = GetAllStudentOrganizationsUsecase(repo)

        stu_org = usecase()
        
        assert len(stu_org) == 3
        assert stu_org[0].name == "Data Science Club IMT"
        assert stu_org[1].name == "AI Lab Mauá"
        assert stu_org[2].name == "Robotics Team Mauá"