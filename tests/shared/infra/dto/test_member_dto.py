from src.shared.domain.entities.member import Member
from src.shared.domain.enums.state_enum import STATE
from src.shared.infra.dto.member_dynamo_dto import MemberDynamoDTO
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock


class Test_MemberDynamoDTO:
    def test_from_entity(self):
        repo = MemberRepositoryMock()

        member_dto = MemberDynamoDTO.from_entity(member=repo.members[0])

        expected_member_dto = MemberDynamoDTO(
            member_id=repo.members[0].member_id,
            name=repo.members[0].name,
            email=repo.members[0].email,
            activities=repo.members[0].activities
        )

        assert member_dto == expected_member_dto

    def test_to_dynamo(self):
        repo = MemberRepositoryMock()

        member_dto = MemberDynamoDTO(
            member_id=repo.members[0].member_id,
            name=repo.members[0].name,
            email=repo.members[0].email,
            activities=repo.members[0].activities
        )

        member_dynamo = member_dto.to_dynamo()

        expected_dict = {
            "entity": "Member",
            "member_id": repo.members[0].member_id,
            "name": repo.members[0].name,
            "email": repo.members[0].email,
            "activities": repo.members[0].activities
        }

        assert member_dynamo == expected_dict

    def test_from_dynamo(self):
        dynamo_dict = {'Item': {'member_id': "f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
                                'name': 'Mateus Martins',
                                'SK': '#' + "f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
                                'PK': 'member#' + "f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
                                'entity': 'Member',
                                'email': 'mateus.martins@gmail.com',
                                'activities': ["8329f5105520a1b72d062628c077ddfa", "e19e98a669ae21f94ffd1659998fd072"]
                                },
                       'ResponseMetadata': {'RequestId': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                            'HTTPStatusCode': 200,
                                            'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 15:40:29 GMT',
                                                            'content-type': 'application/x-amz-json-1.0',
                                                            'x-amz-crc32': '3909675734',
                                                            'x-amzn-requestid': 'aa6a5e5e-943f-4452-8c1f-4e5441ee6042',
                                                            'content-length': '174',
                                                            'server': 'Jetty(9.4.48.v20220622)'},
                                            'RetryAttempts': 0}}
    
        member_dto = MemberDynamoDTO.from_dynamo(member_data=dynamo_dict["Item"])

        expected_member_dto = MemberDynamoDTO(
            member_id="f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
            name='Mateus Martins',
            email='mateus.martins@gmail.com',
            activities=["8329f5105520a1b72d062628c077ddfa", "e19e98a669ae21f94ffd1659998fd072"]
        )

        assert member_dto == expected_member_dto
    
    def test_to_entity(self):
        repo = MemberRepositoryMock()

        member_dto = MemberDynamoDTO(
            member_id=repo.members[0].member_id,
            name=repo.members[0].name,
            email=repo.members[0].email,
            activities=repo.members[0].activities
        )

        member = member_dto.to_entity()

        expected_member = Member(
            member_id=repo.members[0].member_id,
            name=repo.members[0].name,
            email=repo.members[0].email,
            activities=repo.members[0].activities
        )

        assert member.member_id == expected_member.member_id
        assert member.name == expected_member.name
        assert member.email == expected_member.email
        assert member.activities == expected_member.activities

        
    
    def test_from_dynamo_to_entity(self):
        dynamo_item = {'Item': {'member_id': "f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
                                'name': 'Mateus Martins',
                                'SK': '#' + "f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
                                'PK': 'member#' + "f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
                                'entity': 'Member',
                                'email': 'mateus.martins@gmail.com',
                                'activities': ["8329f5105520a1b72d062628c077ddfa", "e19e98a669ae21f94ffd1659998fd072"]
                                }}

        member_dto = MemberDynamoDTO.from_dynamo(member_data=dynamo_item["Item"])

        member = member_dto.to_entity()

        expected_member = Member(
            member_id="f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
            name='Mateus Martins',
            email='mateus.martins@gmail.com',
            activities=["8329f5105520a1b72d062628c077ddfa", "e19e98a669ae21f94ffd1659998fd072"]
        )

        assert member.member_id == expected_member.member_id
        assert member.name == expected_member.name
        assert member.email == expected_member.email
        assert member.activities == expected_member.activities