from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class GetMemberUsecase:

    def __init__(self, repo: IMemberRepository):
        self.repo = repo
    
    def __call__(self, member_id: str):

        if not self.repo.get_member(member_id):
            raise NoItemsFound("Member")
        
        return self.repo.get_member(member_id)
