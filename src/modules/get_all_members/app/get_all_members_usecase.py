from src.shared.domain.entities.member import Member
from src.shared.domain.repositories.member_repository_interface import IMemberRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound



class GetAllMembersUsecase:

    def __init__(self, repo: IMemberRepository):
        self.repo = repo
    
    def __call__(self) -> list[Member]:
        members = self.repo.get_all_members()
        
        if len(members) == 0:
            raise NoItemsFound("members")
        
        return members
