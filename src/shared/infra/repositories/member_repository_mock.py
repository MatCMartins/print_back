from typing import List, Optional

from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class MemberRepositoryMock(IMemberRepository):
        members: List[Member]
    
        def __init__(self):
            self.members = [
                Member(
                    member_id="76d4b5c2-82af-4f36-9d8b-92a7f4b1234a",   
                    name="Alice Johnson",
                    email="alice.johnson@gmail.com",
                    activities=["aB63na9a-82af-4f36-9d8b-92a7f4b1234a"]
                ),
                Member(
                    member_id="a4e53c9f-7b3d-47f6-a1d2-b6c7e5a8f8d3",
                    name="Bob Smith",
                    email="bob.smith@gmail.com",
                    activities=["aB63na9a-82af-4f36-9d8b-92a7f4b1234a"]
                ),
                Member(
                    member_id="b6c7e5a8-f8d3-4e53-c9f7-7b3d47f6a1d2",
                    name="Carla Williams",
                    email="carla.williams@gmail.com",
                    activities=["aB63na9a-82af-4f36-9d8b-92a7f4b1234a", "7d644e62-ef8b-4728-a92b-becb8930c24e"]
                )
            ]
    
        def get_member(self, member_id: str) -> Member:
            for member in self.members:
                if member.member_id == member_id:
                    return member
            return None

    
        def get_all_members(self) -> List[Member]:
            return self.members
    
        def create_member(self, new_member: Member) -> Member:
            self.members.append(new_member)
            return new_member
        
        def update_member_activities(self, member: Member, activities: list) -> Member:
            member.activities = activities
            return member