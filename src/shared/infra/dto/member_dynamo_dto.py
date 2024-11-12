
from src.shared.domain.entities.member import Member
from src.shared.domain.enums.state_enum import STATE


class MemberDynamoDTO:

    member_id: str
    name: str
    email: str
    activities: list

    def __init__(self, member_id: str, name: str, email: str, activities: list):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.activities = activities

    @staticmethod
    def from_entity(member: Member) -> "MemberDynamoDTO":
        """
        Parse data from Member to MemberDynamoDTO
        """
        return MemberDynamoDTO(
            member_id=member.member_id,
            name=member.name,
            email=member.email,
            activities=member.activities
        )
    
    def to_dynamo(self) -> list:
        """
        Parse data from MemberDynamoDTO to list
        """
        return {
            "entity": "Member",
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "activities": self.activities
        }
    
    @staticmethod
    def from_dynamo(member_data: list) -> "MemberDynamoDTO":
        """
        Parse data from DynamoDB to MemberDynamoDTO
        @param member_data: list from DynamoDB
        """
        return MemberDynamoDTO(
            member_id=member_data['member_id'],
            name=member_data['name'],
            email=member_data['email'],
            activities=member_data['activities']
        )
    
    def to_entity(self) -> Member:
        """
        Parse data from MemberDynamoDTO to Member
        """
        return Member(
            member_id=self.member_id,
            name=self.name,
            email=self.email,
            activities=self.activities
        )
    
    def __repr__(self):
        return f"MemberDynamoDTO(member_id={self.member_id}, name={self.name}, email={self.email}, activities={self.activities})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__