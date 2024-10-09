from src.modules.create_student_organization.app.create_student_organization_usecase import CreateStudentOrganizationUsecase
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock
from src.shared.domain.entities.student_organization import StudentOrganization

repo = StudentOrganizationRepositoryMock()

class Test_CreateStudentOrganizationUsecase:
    def test_create_student_organization_usecase(self):
        name = "EcoMauá"
        description = "The EcoMauá is a student organization that aims to promote sustainability and environmental awareness"
        creation_date = 234567890
        logo = "logo"
        instagram = "instagram"
        website_link = "website_link"

        usecase = CreateStudentOrganizationUsecase(repo)
        response = usecase(name, description, creation_date, logo, instagram, website_link)

        assert response.name == name
        assert response.description == description
        assert response.creation_date == creation_date
        assert response.logo == logo
        assert response.instagram == instagram
        assert response.website_link == website_link
            
    
