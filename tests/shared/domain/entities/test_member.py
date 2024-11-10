from src.shared.domain.entities.member import Member
from src.shared.helpers.errors.domain_errors import EntityError
import pytest


class Test_Member:
    def test_member(self):
        member = Member(
            member_id="76d4b5c2-82af-4f36-9d8b-92a7f4b1234a",
            name="John Doe",
            email="john.doe@gmail.com",
            activities=["7cb15e416d62919b1b40298324fbe30b", "e19e98a669ae21f94ffd1659998fd072"]
        )

        assert  member.member_id == "76d4b5c2-82af-4f36-9d8b-92a7f4b1234a"
        assert  member.name == "John Doe"
        assert  member.email == "john.doe@gmail.com"
        assert  member.activities == ["7cb15e416d62919b1b40298324fbe30b", "e19e98a669ae21f94ffd1659998fd072"]

    