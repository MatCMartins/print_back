import pytest
from src.modules.get_member.app.get_member_usecase import GetMemberUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

repo = MemberRepositoryMock()

class Test_GetMemberUsecase:
    def test_get_member_usecase(self):
        usecase = GetMemberUsecase(repo)
        member = usecase(repo.members[0].member_id)

        assert member.member_id == repo.members[0].member_id
        assert member.name == repo.members[0].name
        assert member.email == repo.members[0].email
        assert member.activities == repo.members[0].activities
    
    def test_get_member_usecase_no_items_found(self):
        usecase = GetMemberUsecase(repo)
        with pytest.raises(NoItemsFound) as err:
            usecase("12321")