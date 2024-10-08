import abc
import re

from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError


class StudentOrganization(abc.ABC):
    name: str
    description: str
    logo: str
    instagram: str
    website_link: str

    def __init__(self, name: str, description: str, logo: str, instagram: str, website_link: str):

        if not self.validate_parameters(name):
            raise EntityError("Invalid name")
        self.name = name

        if not self.validate_parameters(description):
            raise EntityError("Invalid description")
        self.description = description

        if not self.validate_parameters(logo):
            raise EntityError("Invalid logo")
        self.logo = logo

        if not self.validate_parameters(instagram):
            raise EntityError("Invalid instagram")
        self.instagram = instagram

        if not self.validate_parameters(website_link):
            raise EntityError("Invalid website_link")
        self.website_link = website_link

        
    @staticmethod
    def validate_parameters(param: str) -> bool:
        if param is None:
            return False
        elif type(param) != str:
            return False

        return True


    def __repr__(self):
        return f"StudentOrganization(name={self.name}, description={self.description}, logo={self.logo}, instagram={self.instagram}, website_link={self.website_link})"
