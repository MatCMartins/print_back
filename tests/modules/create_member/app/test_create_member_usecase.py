from src.modules.create_member.app.create_member_usecase import CreateMemberUsecase
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.entities.member import Member

repo = MemberRepositoryMock()

class Test_CreateMemberUsecase:
    def test_create_member_usecase(self):
        member_id = "f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b"
        name = "Leonardo Stuber"
        email = "leonardo.stuber@gmail.com"
        activities = []

        usecase = CreateMemberUsecase(repo)
        response = usecase(member_id, name, email, activities)

        assert response.member_id == member_id
        assert response.name == name
        assert response.email == email
        assert response.activities == activities
    
