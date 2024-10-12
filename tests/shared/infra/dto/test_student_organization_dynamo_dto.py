

from src.shared.domain.entities.student_organization import StudentOrganization
from src.shared.domain.enums.state_enum import STATE
from src.shared.infra.dto.student_organization_dynamo_dto import StudentOrganizationDynamoDTO
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock


class Test_StudentOrganizationDynamoDTO:
    def test_from_entity(self):
        repo = StudentOrganizationRepositoryMock()

        student_organization_dto = StudentOrganizationDynamoDTO.from_entity(stu_org=repo.stu_orgs[0])

        expected_org_dto = StudentOrganizationDynamoDTO(
            stu_org_id=repo.stu_orgs[0].stu_org_id,
            name=repo.stu_orgs[0].name,
            description=repo.stu_orgs[0].description,
            creation_date=repo.stu_orgs[0].creation_date,
            logo=repo.stu_orgs[0].logo,
            instagram=repo.stu_orgs[0].instagram,
            website_link=repo.stu_orgs[0].website_link
        )

        assert student_organization_dto == expected_org_dto

    def test_to_dynamo(self):
        repo = StudentOrganizationRepositoryMock()

        student_organization_dto = StudentOrganizationDynamoDTO(
            stu_org_id=repo.stu_orgs[0].stu_org_id,
            name=repo.stu_orgs[0].name,
            description=repo.stu_orgs[0].description,
            creation_date=repo.stu_orgs[0].creation_date,
            logo=repo.stu_orgs[0].logo,
            instagram=repo.stu_orgs[0].instagram,
            website_link=repo.stu_orgs[0].website_link
        )

        student_organization_dynamo = student_organization_dto.to_dynamo()

        expected_dict = {
            "entity": "student_organization",
            "stu_org_id": repo.stu_orgs[0].stu_org_id,
            "name": repo.stu_orgs[0].name,
            "description": repo.stu_orgs[0].description,
            "creation_date": repo.stu_orgs[0].creation_date,
            "logo": repo.stu_orgs[0].logo,
            "instagram": repo.stu_orgs[0].instagram,
            "website_link": repo.stu_orgs[0].website_link
        }

        assert student_organization_dynamo == expected_dict

    def test_from_dynamo(self):
        dynamo_dict = {'Item': {'stu_org_id': 1234,
                                'name': 'mateus',
                                'SK': '#' + str(1234),
                                'PK': 'stu_org#' + str(1234),
                                'entity': 'student_organization',
                                'description': 'description',
                                'creation_date': 1234,
                                'logo': 'logo',
                                'instagram': 'instagram',
                                'website_link': 'website_link'
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

        stu_org_dto = StudentOrganizationDynamoDTO.from_dynamo(stu_org_data=dynamo_dict["Item"])

        expected_stu_org_dto = StudentOrganizationDynamoDTO(
            stu_org_id=1234,
            name='mateus',
            description='description',
            creation_date=1234,
            logo='logo',
            instagram='instagram',
            website_link='website_link'
        )

        assert stu_org_dto == expected_stu_org_dto

    def test_to_entity(self):
        repo = StudentOrganizationRepositoryMock()

        stu_org_dto = StudentOrganizationDynamoDTO(
            stu_org_id=repo.stu_orgs[0].stu_org_id,
            name=repo.stu_orgs[0].name,
            description=repo.stu_orgs[0].description,
            creation_date=repo.stu_orgs[0].creation_date,
            logo=repo.stu_orgs[0].logo,
            instagram=repo.stu_orgs[0].instagram,
            website_link=repo.stu_orgs[0].website_link
        )

        stu_org = stu_org_dto.to_entity()

        assert stu_org.name == repo.stu_orgs[0].name
        assert stu_org.description == repo.stu_orgs[0].description
        assert stu_org.creation_date == repo.stu_orgs[0].creation_date
        assert stu_org.logo == repo.stu_orgs[0].logo
        assert stu_org.instagram == repo.stu_orgs[0].instagram
        assert stu_org.website_link == repo.stu_orgs[0].website_link

    def test_from_dynamo_to_entity(self):
        dynamo_item = {'Item': {'stu_org_id': 1234,
                                'name': 'mateus',
                                'SK': '#' + str(1234),
                                'PK': 'stu_org#' + str(1234),
                                'entity': 'student_organization',
                                'description': 'description',
                                'creation_date': 1234,
                                'logo': 'logo',
                                'instagram': 'instagram',
                                'website_link': 'website_link'
                                }}

        stu_org_dto = StudentOrganizationDynamoDTO.from_dynamo(stu_org_data=dynamo_item["Item"])

        stu_org = stu_org_dto.to_entity()

        expected_stu_org = StudentOrganization(
            name='mateus',
            description='description',
            creation_date=1234,
            logo='logo',
            instagram='instagram',
            website_link='website_link',
        )

        assert stu_org.stu_org_id == expected_stu_org.stu_org_id
        assert stu_org.name == expected_stu_org.name
        assert stu_org.description == expected_stu_org.description
        assert stu_org.creation_date == expected_stu_org.creation_date
        assert stu_org.logo == expected_stu_org.logo
        assert stu_org.instagram == expected_stu_org.instagram
        assert stu_org.website_link == expected_stu_org.website_link


    def test_from_entity_to_dynamo(self):
        repo = StudentOrganizationRepositoryMock()

        stu_org_dto = StudentOrganizationDynamoDTO.from_entity(stu_org=repo.stu_orgs[0])

        stu_org_dynamo = stu_org_dto.to_dynamo()

        expected_dict = {
            "entity": "student_organization",
            "stu_org_id": repo.stu_orgs[0].stu_org_id,
            "name": repo.stu_orgs[0].name,
            "description": repo.stu_orgs[0].description,
            "creation_date": repo.stu_orgs[0].creation_date,
            "logo": repo.stu_orgs[0].logo,
            "instagram": repo.stu_orgs[0].instagram,
            "website_link": repo.stu_orgs[0].website_link
        }

        assert stu_org_dynamo == expected_dict
