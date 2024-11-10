from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.domain.entities.member import Member

class CreateMemberUsecase:

    def __init__(self, repo: IMemberRepository):
        self.repo = repo
    def __call__(self, member_id: str, name: str, email: str, activities: list):

        if self.repo.duplicate_member(member_id):
            raise DuplicatedItem("member_id")
        
        member = Member(
            member_id=member_id,
            name=name,
            email=email,
            activities=activities
        )
        
        return self.repo.create_member(member)