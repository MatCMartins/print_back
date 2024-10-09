from src.shared.domain.entities.student_organization import StudentOrganization
from src.shared.domain.repositories.student_organization_repository_interface import IStudentOrganizationRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound



class GetAllStudentOrganizationsUsecase:

    def __init__(self, repo: IStudentOrganizationRepository):
        self.repo = repo
    
    def __call__(self) -> list[StudentOrganization]:
        student_organizations = self.repo.get_all_stu_orgs()
        
        if len(student_organizations) == 0:
            raise NoItemsFound("student organizations")
        
        return student_organizations
