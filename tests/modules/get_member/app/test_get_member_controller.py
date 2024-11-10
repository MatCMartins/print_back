from src.modules.get_member.app.get_member_controller import GetMemberController
from src.modules.get_member.app.get_member_usecase import GetMemberUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

repo = MemberRepositoryMock()

class Test_GetMemberController:
    def test_get_member_controller(self):
        usecase = GetMemberUsecase(repo)
        controller = GetMemberController(usecase)

        request = HttpRequest(query_params={"member_id": repo.members[0].member_id})

        response = controller(request)

        assert response.status_code == 200
        assert response.body["name"] == repo.members[0].name
        assert response.body["email"] == repo.members[0].email
        assert response.body["activities"] == repo.members[0].activities
        
        

    def test_get_member_controller_no_items_found(self):
        usecase = GetMemberUsecase(repo)
        controller = GetMemberController(usecase)

        request = HttpRequest(query_params={"member_id": "12321"})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "No items found for member_id"
    
    def test_get_member_controller_wrong_parameter_type(self):
        usecase = GetMemberUsecase(repo)
        controller = GetMemberController(usecase)

        request = HttpRequest(query_params={"member_id": 1231})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field member_id isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
        
    def test_get_member_controller_missing_parameter(self):
        usecase = GetMemberUsecase(repo)
        controller = GetMemberController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field member_id is missing"