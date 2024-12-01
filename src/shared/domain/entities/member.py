import abc

from src.shared.helpers.errors.domain_errors import EntityError

class Member(abc.ABC):
    member_id: str
    name: str
    email: str
    activities: list

    def __init__(self, member_id: str, name: str, email: str, activities: list):

        if not self.validate_parameters(name):
            raise EntityError("Invalid name")
        self.name = name

        if not self.validate_parameters(email):
            raise EntityError("Invalid email")
        self.email = email

        if not self.validate_activities(activities):
            raise EntityError("Invalid activities")
        self.activities = activities

        if not self.validate_id(member_id):
            raise EntityError("Invalid member_id")
        self.member_id = member_id

                
    @staticmethod
    def validate_parameters(param: str) -> bool:
        if param is None:
            return False
        elif type(param) != str:
            return False
        return True

    @staticmethod
    def validate_activities(param: list) -> bool:
        if param is None:
            return False
        elif type(param) != list:
            return False
        return True


    @staticmethod
    def validate_id(id: str) -> bool:
        if id is None:
            return False
        elif type(id) != str:
            return False
        elif len(id) != 36:
            return False
        return True

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "activities": self.activities
        }

    def __repr__(self):
        return f"Member(member_id={self.member_id}, name={self.name}, email={self.email}, activities={self.activities})"
