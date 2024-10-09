from src.shared.domain.entities.student_organization import StudentOrganization
from src.shared.domain.repositories.student_organization_repository_interface import IStudentOrganizationRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound



class GetStudentOrganizationsUsecase:

    def __init__(self, repo: IStudentOrganizationRepository):
        self.repo = repo
    
    def __call__(self, stu_org_id: str):
        try:
            return self.repo.get_stu_org(stu_org_id)
        except NoItemsFound as e:
            return e.to_dict()
