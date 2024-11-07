import abc
import hashlib
from typing import Optional

from src.shared.helpers.errors.domain_errors import EntityError

class Course(abc.ABC):
    course_id: str
    name: str
    course_photo: str
    coordinator: str
    coordinator_photo: str
    description: str
    link: Optional[str] = None

    def __init__(self, name: str, course_photo: str, coordinator: str, coordinator_photo: str,description: str, link: Optional[str] = None):

        if not self.validate_parameters(name):
            raise EntityError("Invalid name")
        self.name = name

        if not self.validate_parameters(description):
            raise EntityError("Invalid description")
        self.description = description

        if not self.validate_parameters(coordinator):
            raise EntityError("Invalid coordinator")
        self.coordinator = coordinator

        if not self.validate_parameters(coordinator_photo):
            raise EntityError("Invalid coordinator_photo")
        self.coordinator_photo = coordinator_photo

        if not self.validate_link(link):
            raise EntityError("Invalid link")
        self.link = link

        if not self.validate_parameters(course_photo):
            raise EntityError("Invalid course_photo")
        self.course_photo = course_photo

        
        
        self.course_id = hashlib.md5((name).encode()).hexdigest()
        
    @staticmethod
    def validate_parameters(param: str) -> bool:
        if param is None:
            return False
        elif type(param) != str:
            return False
        return True

    @staticmethod
    def validate_link(param: str) -> bool:
        if param is None:
            return True
        if type(param) != str:
            return False
        return True

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "name": self.name,
            "course_photo": self.course_photo,
            "coordinator": self.coordinator,
            "coordinator_photo": self.coordinator_photo,
            "description": self.description,
            "link": self.link
        }
    def __repr__(self):
        return f"StudentOrganization(course_id={self.course_id}, name={self.name}, course_photo={self.course_photo}, coordinator={self.coordinator}, coordinator_photo={self.coordinator_photo}, description={self.description}, link={self.link})"
