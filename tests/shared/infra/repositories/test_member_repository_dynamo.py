import os

import pytest

from src.shared.infra.repositories.member_repository_dynamo import MemberRepositoryDynamo
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
from src.shared.domain.entities.member import Member


class Test_MemberRepositoryDynamo:

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_create_member(self):

        member_repository = MemberRepositoryDynamo()
        member_repository_mock = MemberRepositoryMock()

        member = Member(
            member_id="f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
            name="Carl Lewis",
            email="carl.lewis@gmail.com",
            activities=[]
        )

        resp = member_repository.create_member(member)

        assert member_repository_mock.members[0].name == resp.name

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_member(self):

        member_repository = MemberRepositoryDynamo()
        member_repository_mock = MemberRepositoryMock()
        resp = member_repository.get_member(member_repository_mock.members[0].member_id)
        
        assert member_repository_mock.members[0].name == resp.name

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_all_members(self):
        
        member_repository = MemberRepositoryDynamo()
        member_repository_mock = MemberRepositoryMock()
        resp = member_repository.get_all_members()

        assert len(member_repository_mock.members) == len(resp)