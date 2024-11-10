from src.modules.get_member.app.get_member_viewmodel import GetMemberViewmodel
from src.shared.domain.entities.member import Member


class Test_GetMemberViewmodel:
    def test_get_member_viewmodel(self):
        member = Member(
            member_id="f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
            name="Leonardo Stuber",
            email="leonardo.stuber@gmail.com",
            activities=[]
        )

        viewmodel = GetMemberViewmodel(
            member_id=member.member_id,
            name=member.name,
            email=member.email,
            activities=member.activities
        ).to_dict()

        expected = {
            "member_id": member.member_id,
            "name": member.name,
            "email": member.email,
            "activities": member.activities
        }	

        assert viewmodel == expected
