from src.modules.get_all_members.app.get_all_members_viewmodel import GetAllMembersViewmodel
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock
 

class Test_GetAllMembersViewmodel:
    def test_get_all_members_viewmodel(self):
        members = MemberRepositoryMock().members
        viewmodel = GetAllMembersViewmodel(members).to_dict()
        expected ={
            "members": [
                {
                    "member_id": "76d4b5c2-82af-4f36-9d8b-92a7f4b1234a",
                    "name": "Alice Johnson",
                    "email": "alice.johnson@gmail.com",
                    "activities": ["8329f5105520a1b72d062628c077ddfa", "e19e98a669ae21f94ffd1659998fd072"]
                },
                {
                    "member_id": "a4e53c9f-7b3d-47f6-a1d2-b6c7e5a8f8d3",
                    "name": "Bob Smith",
                    "email": "bob.smith@gmail.com",
                    "activities": ["8329f5105520a1b72d062628c077ddfa"]
                },
                {
                    "member_id": "b6c7e5a8-f8d3-4e53-c9f7-7b3d47f6a1d2",
                    "name": "Carla Williams",
                    "email": "carla.williams@gmail.com",
                    "activities": ["e19e98a669ae21f94ffd1659998fd072", "7cb15e416d62919b1b40298324fbe30b"]
                }
            ]
        }


        assert viewmodel == expected
