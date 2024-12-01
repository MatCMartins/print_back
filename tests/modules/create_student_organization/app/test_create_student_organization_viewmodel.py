import re
from src.modules.create_student_organization.app.create_student_organization_viewmodel import CreateStudentOrganizationViewModel
from src.shared.domain.entities.student_organization import StudentOrganization

class Test_CreateStudentOrganizationViewmodel:
    def test_create_student_organization_viewmodel(self):
        stu_org = StudentOrganization(
            stu_org_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            name="Enactus IMT",
            description="Enactus IMT is a student organization that aims to develop projects that help the community.",
            creation_date=123456789,
            logo="https://enactusimt.com/logo.png",
            instagram="https://instagram.com/enactusimt",
            website_link="https://enactusimt.com"
        )

        viewmodel = CreateStudentOrganizationViewModel(
            stu_org_id=stu_org.stu_org_id,
            name=stu_org.name,
            description=stu_org.description,
            creation_date=stu_org.creation_date,
            logo=stu_org.logo,
            instagram=stu_org.instagram,
            website_link=stu_org.website_link
        )

        assert re.match(r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$', viewmodel.to_dict()["stu_org_id"])

        expected = {
            "stu_org_id": stu_org.stu_org_id,
            "name": "Enactus IMT",
            "description": "Enactus IMT is a student organization that aims to develop projects that help the community.",
            "creation_date": 123456789,
            "logo": "https://enactusimt.com/logo.png",
            "instagram": "https://instagram.com/enactusimt",
            "website_link": "https://enactusimt.com"
        }	

        assert viewmodel.to_dict() == expected