from src.modules.create_member.app.create_member_controller import CreateMemberController
from src.modules.create_member.app.create_member_usecase import CreateMemberUsecase
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

repo = MemberRepositoryMock()

class Test_CreateMemberController:
    def test_create_member_controller(self):
        usecase = CreateMemberUsecase(repo)
        controller = CreateMemberController(usecase)

        request = HttpRequest(query_params={
            "member_id": "f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
            "name": "Leonardo Stuber",
            "email": "leonardo.stuber@gmail.com",
            "activities": []
        })

        response = controller(request)

        assert response.status_code == 201

    