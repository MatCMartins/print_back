import abc
import re

from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError


class StudentOrganization(abc.ABC):
    stu_org_id: int
    name: str
    description: str
    creation_date: int
    logo: str
    instagram: str
    website_link: str

    def __init__(self, name: str, description: str, creation_date: int, logo: str, instagram: str, website_link: str):

        if not self.validate_parameters(name):
            raise EntityError("Invalid name")
        self.name = name

        if not self.validate_parameters(description):
            raise EntityError("Invalid description")
        self.description = description

        if not self.validate_creation_date(creation_date):
            raise EntityError("Invalid creation_date")
        self.creation_date = creation_date

        if not self.validate_parameters(logo):
            raise EntityError("Invalid logo")
        self.logo = logo

        if not self.validate_parameters(instagram):
            raise EntityError("Invalid instagram")
        self.instagram = instagram

        if not self.validate_parameters(website_link):
            raise EntityError("Invalid website_link")
        self.website_link = website_link

        #create personalized id
        self.stu_org_id = hash(name + str(creation_date))

        
    @staticmethod
    def validate_parameters(param: str) -> bool:
        if param is None:
            return False
        elif type(param) != str:
            return False
        return True

    @staticmethod
    def validate_creation_date(param: int) -> bool:
        if param is None:
            return False
        elif type(param) != int:
            return False
        return True


    def __repr__(self):
        return f"StudentOrganization(stu_org_id={self.stu_org_id}, name={self.name}, description={self.description}, creation_date={self.creation_date} logo={self.logo}, instagram={self.instagram}, website_link={self.website_link})"
