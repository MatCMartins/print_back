from uuid import uuid4
from src.shared.domain.repositories.student_organization_repository_interface import IStudentOrganizationRepository
from src.shared.domain.entities.student_organization import StudentOrganization

class CreateStudentOrganizationUsecase:

    def __init__(self, repo: IStudentOrganizationRepository):
        self.repo = repo
    def __call__(self, name: str, description: str, creation_date: str, logo: str, instagram: str, website_link: str):

        stu_org_id = str(uuid4())
        
        new_org = StudentOrganization(
            stu_org_id=stu_org_id,
            name=name,
            description=description,
            creation_date=creation_date,
            logo=logo,
            instagram=instagram,
            website_link=website_link
        )
        
        return self.repo.create_stu_org(new_org)