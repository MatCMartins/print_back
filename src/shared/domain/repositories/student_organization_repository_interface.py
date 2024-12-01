from abc import ABC, abstractmethod
from typing import List, Optional

from src.shared.domain.entities.student_organization import StudentOrganization


class IStudentOrganizationRepository(ABC):

    @abstractmethod
    def get_stu_org(self, stu_org_id: str) -> StudentOrganization:
        """
        If stu_org_id not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def get_all_stu_orgs(self) -> List[StudentOrganization]:
        pass

    @abstractmethod
    def create_stu_org(self, new_stu_org: StudentOrganization) -> StudentOrganization:
        pass

    @abstractmethod
    def delete_stu_org(self, stu_org_id: str) -> StudentOrganization:
        """
        If stu_org_id not found raise NoItemsFound
        """
        pass

    @abstractmethod
    def update_stu_org(self, stu_org_id: str, new_name: Optional[str] = None, new_description: Optional[str] = None, new_creation_date: int = None, new_logo: Optional[str] = None, new_instagram: Optional[str] = None) -> StudentOrganization:
        """
        If stu_org_id not found raise NoItemsFound
        """
        pass
