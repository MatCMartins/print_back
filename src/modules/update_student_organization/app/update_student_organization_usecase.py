from typing import Optional
from src.shared.domain.entities.student_organization import StudentOrganization
from src.shared.domain.repositories.student_organization_repository_interface import IStudentOrganizationRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class UpdateStudentOrganizationUsecase:

    def __init__(self, repo: IStudentOrganizationRepository):
        self.repo = repo
    
    def __call__(self, stu_org_id: str, name: Optional[str] = None, description: Optional[str] = None, creation_date: Optional[str] = None, logo: Optional[str] = None, instagram: Optional[str] = None, website_link: Optional[str] = None):
        
        if not self.repo.get_stu_org(stu_org_id):
            raise NoItemsFound("Student Organization")
        
        return self.repo.update_stu_org(stu_org_id, name, description, creation_date, logo, instagram, website_link)