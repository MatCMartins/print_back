import os

import pytest

from src.shared.infra.repositories.student_organization_repository_dynamo import StudentOrganizationRepositoryDynamo
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock
from src.shared.domain.entities.student_organization import StudentOrganization


class Test_StudentOrganizationRepositoryDynamo:

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_create_stu_org(self):

        stu_org_repository = StudentOrganizationRepositoryDynamo()
        stu_org_repository_mock = StudentOrganizationRepositoryMock()

        stu_org = StudentOrganization(
            name="Maua Tech Club", 
            description="A club for tech enthusiasts", 
            creation_date=1620009600, 
            logo="https://mauatech.com/logo.png",
            instagram="https://instagram.com/mauatech",
            website_link="https://mauatech.com"
        )

        resp = stu_org_repository.create_stu_org(stu_org)

        assert stu_org_repository_mock.stu_orgs[0].name == resp.name

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_stu_org(self):

        stu_org_repository = StudentOrganizationRepositoryDynamo()
        stu_org_repository_mock = StudentOrganizationRepositoryMock()
        resp = stu_org_repository.get_stu_org(stu_org_repository_mock.stu_orgs[0].stu_org_id)
        assert stu_org_repository_mock.stu_orgs[0].name == resp.name

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_delete_stu_org(self):
        
        stu_org_repository = StudentOrganizationRepositoryDynamo()
        stu_org_repository_mock = StudentOrganizationRepositoryMock()
        resp = stu_org_repository.delete_stu_org(stu_org_repository_mock.stu_orgs[1].stu_org_id)

        assert stu_org_repository_mock.stu_orgs[1].name == resp.name

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_get_all_stu_orgs(self):
        
        stu_org_repository = StudentOrganizationRepositoryDynamo()
        stu_org_repository_mock = StudentOrganizationRepositoryMock()
        resp = stu_org_repository.get_all_stu_orgs()

        assert len(stu_org_repository_mock.stu_orgs) == len(resp)

    @pytest.mark.skip(reason="Needs dynamoDB")
    def test_update_stu_org(self):
        
        stu_org_repository = StudentOrganizationRepositoryDynamo()
        stu_org_repository_mock = StudentOrganizationRepositoryMock()
        resp = stu_org_repository.update_stu_org(stu_org_id=stu_org_repository_mock.stu_orgs[0].stu_org_id, new_name="Maua Tech")

        assert resp.name == "Maua Tech"