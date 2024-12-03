import pytest
from src.modules.update_member_activities.app.update_member_activities_usecase import UpdateMemberActivitiesUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock

class Test_UpdateMemberActivitiesUsecase:
    def test_update_member_activities_usecase(self):
        repo_member = MemberRepositoryMock()
        repo_event = EventRepositoryMock()
        usecase = UpdateMemberActivitiesUsecase(repo_member, repo_event)

        event = repo_event.events[0].event_id
        member = repo_member.members[0].member_id
        activities = repo_member.members[2].activities


        response = usecase(
            event_id=event,
            member_id=member,
            activities=activities
        )

        assert response.member_id == member
        assert response.activities == activities
    
