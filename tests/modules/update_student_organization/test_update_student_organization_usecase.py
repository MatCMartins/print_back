import pytest
from src.modules.update_student_organization.app.update_student_organization_usecase import UpdateStudentOrganizationUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock
from src.shared.domain.entities.student_organization import StudentOrganization

class Test_UpdateStudentOrganizationUsecase:
    def test_update_student_organization_usecase(self):
        repo = StudentOrganizationRepositoryMock()
        usecase = UpdateStudentOrganizationUsecase(repo)
        first_stu_org_id = repo.stu_orgs[0].stu_org_id

        name="Maua Jr"
        description="This student organization is a junior company"
        creation_date=234567890
        logo="logo"
        instagram="instagram"

        response = usecase(
            stu_org_id=first_stu_org_id,
            name=name,
            description=description,
            creation_date=creation_date,
            logo=logo,
            instagram=instagram,
        )
        
        assert repo.stu_orgs[0].name == "Maua Jr"
        assert repo.stu_orgs[0].description == "This student organization is a junior company"
        assert repo.stu_orgs[0].creation_date == 234567890
        assert repo.stu_orgs[0].logo == "logo"
        assert repo.stu_orgs[0].instagram == "instagram"
    
    def test_update_student_organization_no_stu_org_id(self):
        repo = StudentOrganizationRepositoryMock()
        usecase = UpdateStudentOrganizationUsecase(repo)

        name="Maua Jr"
        description="This student organization is a junior company"
        creation_date=234567890
        logo="logo"
        instagram="instagram"

  
        with pytest.raises(NoItemsFound):
            response = usecase(
            stu_org_id=None,
            name=name,
            description=description,
            creation_date=creation_date,
            logo=logo,
            instagram=instagram,
        )
