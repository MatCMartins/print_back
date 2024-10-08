from typing import List

from src.shared.domain.entities.student_organization import StudentOrganization
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.student_organization_repository_interface import IStudentOrganizationRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class StudentOrganizationRepositoryMock(IStudentOrganizationRepository):
    stu_orgs: List[StudentOrganization]

    def __init__(self):
        self.stu_orgs = [
            StudentOrganization(
                name="Data Science Club IMT", 
                description="Organization dedicated to promoting knowledge and projects in the field of data science and machine learning.", 
                creation_date=1620009600, 
                logo="https://datascienceclubimt.com/logo.png", 
                instagram="https://instagram.com/datascienceclubimt", 
                website_link="https://datascienceimt.com"
            ),
            StudentOrganization(
                name="AI Lab Mauá", 
                description="A community focused on artificial intelligence research and applications, encouraging students to participate in AI projects.", 
                creation_date=1609459200, 
                logo="https://ailabmaua.com/logo.png", 
                instagram="https://instagram.com/ailabmaua", 
                website_link="https://ailabmaua.com"
            ),
            StudentOrganization(
                name="Robotics Team Mauá", 
                description="A student organization focused on building and programming autonomous robots to compete in national and international competitions.", 
                creation_date=1619827200, 
                logo="https://roboticsteam.com/logo.png", 
                instagram="https://instagram.com/roboticsteammaua", 
                website_link="https://roboticsteammaua.com"
            )
        ]

    def get_stu_org(self, stu_org_id: int) -> StudentOrganization:
        for org in self.stu_orgs:
            if org.stu_org_id == stu_org_id:
                return org
        raise NoItemsFound("stu_org_id")

    def get_all_stu_orgs(self) -> List[StudentOrganization]:
        return self.stu_orgs

    def create_stu_org(self, new_org: StudentOrganization) -> StudentOrganization:
        self.stu_orgs.append(new_org)
        return new_org

    def delete_stu_org(self, stu_org_id: int) -> StudentOrganization:
        for idx, org in enumerate(self.stu_orgs):
            if org.stu_org_id == stu_org_id:
                return self.stu_orgs.pop(idx)

        raise NoItemsFound("stu_org_id")

    def update_stu_org(self, stu_org_id: int, new_name: str = None, new_description: str = None, new_creation_date: int = None, new_logo: str = None, new_instagram: str = None, new_website_link: str = None) -> StudentOrganization:
        for stu_org in self.stu_orgs:
            if stu_org.stu_org_id == stu_org_id:
                if new_name is not None:
                    stu_org.name = new_name
                if new_description is not None:
                    stu_org.description = new_description
                if new_creation_date is not None:
                    stu_org.creation_date = new_creation_date
                if new_logo is not None:
                    stu_org.logo = new_logo
                if new_instagram is not None:
                    stu_org.instagram = new_instagram
                if new_website_link is not None:
                    stu_org.website_link = new_website_link
                return stu_org

        raise NoItemsFound("stu_org_id")
