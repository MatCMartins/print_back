from src.shared.domain.entities.student_organization import StudentOrganization
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError
import pytest


class Test_StudentOrganization:
    def test_student_organization(self):
        StudentOrganization(stu_org_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua")

    def test_name_is_none(self):
        with pytest.raises(EntityError):
            StudentOrganization(stu_org_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", name=None, description="Organization focused on developing web applications", creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua")

    def test_name_is_not_str(self):
        with pytest.raises(EntityError):
            StudentOrganization(stu_org_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", name=1, description="Organization focused on developing web applications", creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua")

    def test_description_is_none(self):
        with pytest.raises(EntityError):
            StudentOrganization(stu_org_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", name="Dev Community Mauá", description=None, creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua")

    def test_description_is_not_valid(self):
        with pytest.raises(EntityError):
            StudentOrganization(stu_org_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", name="Dev Community Mauá", description=321312, creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua")

    def test_creation_date_is_none(self):
        with pytest.raises(EntityError):
            StudentOrganization(stu_org_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date=None, logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua")

    def test_creation_date_is_not_valid(self):
        with pytest.raises(EntityError):
            StudentOrganization(stu_org_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date="1612137600", logo="https://devcommunitymaua.com.br/logo.png", instagram="https://instagram.com/devcommunitymaua")

    def test_logo_is_none(self):
        with pytest.raises(EntityError):
            StudentOrganization(stu_org_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date=1612137600, logo=None, instagram="https://instagram.com/devcommunitymaua")

    def test_logo_is_not_valid(self):
        with pytest.raises(EntityError):
            StudentOrganization(stu_org_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date=1612137600, logo=123, instagram="https://instagram.com/devcommunitymaua")

    def test_instagram_is_none(self):
        with pytest.raises(EntityError):
            StudentOrganization(stu_org_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram=None)

    def test_instagram_is_not_valid(self):
        with pytest.raises(EntityError):
            StudentOrganization(stu_org_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496", name="Dev Community Mauá", description="Organization focused on developing web applications", creation_date=1612137600, logo="https://devcommunitymaua.com.br/logo.png", instagram=12)

