import hashlib
from src.modules.create_student_organization.app.create_student_organization_viewmodel import CreateStudentOrganizationViewModel
from src.shared.domain.entities.student_organization import StudentOrganization

class Test_CreateStudentOrganizationViewmodel:
    def test_create_student_organization_viewmodel(self):
        stu_org = StudentOrganization(
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

        expected = {
            "stu_org_id": hashlib.md5(("Enactus IMT" + str(123456789)).encode()).hexdigest(),
            "name": "Enactus IMT",
            "description": "Enactus IMT is a student organization that aims to develop projects that help the community.",
            "creation_date": 123456789,
            "logo": "https://enactusimt.com/logo.png",
            "instagram": "https://instagram.com/enactusimt",
            "website_link": "https://enactusimt.com"
        }	

        assert viewmodel.to_dict() == expected