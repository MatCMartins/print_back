from src.modules.update_member_activities.app.update_member_activities_controller import UpdateMemberActivitiesController
from src.modules.update_member_activities.app.update_member_activities_usecase import UpdateMemberActivitiesUsecase
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class Test_UpdateMemberActivitiesController:
    def test_update_member_activities_controller(self):
        repo_member = MemberRepositoryMock()
        repo_event = EventRepositoryMock()
        usecase = UpdateMemberActivitiesUsecase(repo_member, repo_event)
        controller = UpdateMemberActivitiesController(usecase)

        response = HttpRequest(query_params={
            "event_id": repo_event.events[0].event_id,
            "member_id": repo_member.members[0].member_id,
            "activities": repo_member.members[2].activities,
        })

        response = controller(response)

        assert response.status_code == 200
        assert response.body["member_id"] == repo_member.members[0].member_id
        assert response.body["activities"] == repo_member.members[2].activities
