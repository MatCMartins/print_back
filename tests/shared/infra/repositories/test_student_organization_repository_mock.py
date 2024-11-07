from src.shared.domain.entities.student_organization import StudentOrganization
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock
import pytest


class Test_StudentOrganizationRepositoryMock:
    def test_get_stu_org(self):
        repo = StudentOrganizationRepositoryMock()
        stu_org = repo.get_stu_org(repo.stu_orgs[0].stu_org_id)

        assert stu_org.name == "Data Science Club IMT"
        assert stu_org.description == "Organization dedicated to promoting knowledge and projects in the field of data science and machine learning."
        assert stu_org.creation_date == 1620009600
        assert stu_org.logo == "https://datascienceclubimt.com/logo.png"
        assert stu_org.instagram == "https://instagram.com/datascienceclubimt"
        assert stu_org.website_link == "https://datascienceimt.com"

    def test_get_stu_org_not_found(self):
        repo = StudentOrganizationRepositoryMock()
        assert repo.get_stu_org(32) == None

    def test_get_all_stu_orgs(self):
        repo = StudentOrganizationRepositoryMock()
        stu_orgs = repo.get_all_stu_orgs()
        assert len(stu_orgs) == 3

    def test_create_stu_org(self):
        repo = StudentOrganizationRepositoryMock()
        stu_org = StudentOrganization(
            name="Maua Tech",
            description="Technology organization focused on promoting knowledge and projects in the field of technology and innovation.",
            creation_date=1620009600,
            logo="https://mauatech.com/logo.png",
            instagram="https://instagram.com/mauatech",
            website_link="https://mauatech.com"

        )

        repo.create_stu_org(stu_org)

        assert repo.stu_orgs[3].name == "Maua Tech"
        assert repo.stu_orgs[3].description == "Technology organization focused on promoting knowledge and projects in the field of technology and innovation."
        assert repo.stu_orgs[3].creation_date == 1620009600
        assert repo.stu_orgs[3].logo == "https://mauatech.com/logo.png"
        assert repo.stu_orgs[3].instagram == "https://instagram.com/mauatech"
        assert repo.stu_orgs[3].website_link == "https://mauatech.com"


    def test_delete_stu_org(self):
        repo = StudentOrganizationRepositoryMock()
        stu_org = repo.delete_stu_org(stu_org_id=repo.stu_orgs[0].stu_org_id)

        assert stu_org.name == "Data Science Club IMT"
        assert len(repo.stu_orgs) == 2

    def test_delete_stu_org_not_found(self):
        repo = StudentOrganizationRepositoryMock()
        assert repo.delete_stu_org(32) == None

    def test_update_stu_org(self):
        repo = StudentOrganizationRepositoryMock()
        stu_org = repo.update_stu_org(repo.stu_orgs[0].stu_org_id, "Maua Tech")

        assert stu_org.name == "Maua Tech"
        assert repo.stu_orgs[0].name == "Maua Tech"

    def test_update_stu_org_not_found(self):
        repo = StudentOrganizationRepositoryMock()

        assert repo.update_stu_org(32, "Maua Tech") == None

