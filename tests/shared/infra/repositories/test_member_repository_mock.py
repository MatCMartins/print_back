from src.shared.domain.entities.member import Member
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
import pytest


class Test_MemberRepositoryMock:

    def test_get_member(self):
        repo = MemberRepositoryMock()
        member = repo.get_member(repo.members[0].member_id)

        assert member.member_id == "76d4b5c2-82af-4f36-9d8b-92a7f4b1234a"
        assert member.name == "Alice Johnson"
        assert member.email == "alice.johnson@gmail.com"
        assert member.activities == ["aB63na9a-82af-4f36-9d8b-92a7f4b1234a"]

    def test_get_member_not_found(self):
        repo = MemberRepositoryMock()

        assert repo.get_member("Member") == None
    
    def test_get_all_members(self):
        repo = MemberRepositoryMock()
        members = repo.get_all_members()
        assert len(members) == 3

    def test_create_member(self):
        repo = MemberRepositoryMock()
        member = Member(
            member_id="f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
            name="Carl Lewis",
            email="carl.lewis@gmail.com",
            activities=[]
        )

        repo.create_member(member)

        assert len(repo.members) == 4
        assert repo.members[3].member_id == "f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b"
        assert repo.members[3].name == "Carl Lewis"
        assert repo.members[3].email == "carl.lewis@gmail.com"
        assert repo.members[3].activities == []