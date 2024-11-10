from src.modules.get_all_members.app.get_all_members_controller import GetAllMembersController
from src.modules.get_all_members.app.get_all_members_usecase import GetAllMembersUsecase
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

repo = MemberRepositoryMock()

class Test_GetAllMembersController:
    def test_get_all_members_controller(self):
        usecase = GetAllMembersUsecase(repo)
        controller = GetAllMembersController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request)

        assert response.status_code == 200