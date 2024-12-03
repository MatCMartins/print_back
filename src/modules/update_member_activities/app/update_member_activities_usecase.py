from typing import Optional
from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.domain.repositories.event_repository_interface import IEventRepository
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class UpdateMemberActivitiesUsecase:

    def __init__(self, repo_member: IMemberRepository, repo_event: IEventRepository):
        self.repo_member = repo_member
        self.repo_event = repo_event
    
    def __call__(self, event_id: str, member_id: str, activities: list) -> Member:
        
        
        if not self.repo_event.get_event(event_id):
            raise NoItemsFound("Event")
        member = self.repo_member.get_member(member_id)
        if not member:
            raise NoItemsFound("Member")
        if (event_id not in activities) and ((event_id not in activities) and (event_id not in member.activities)):
            raise NoItemsFound("activities")
        
        
        return self.repo_member.update_member_activities(member, activities)
