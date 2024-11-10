from src.modules.get_all_members.app.get_all_members_usecase import GetAllMembersUsecase
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

repo = MemberRepositoryMock()

class Test_GetAllMembersUsecase:
    def test_get_all_members_usecase(self):
        usecase = GetAllMembersUsecase(repo)

        member = usecase()
        
        assert len(member) == 3
        assert member[0].name == "Alice Johnson"
        assert member[1].name == "Bob Smith"
        assert member[2].name == "Carla Williams"

        