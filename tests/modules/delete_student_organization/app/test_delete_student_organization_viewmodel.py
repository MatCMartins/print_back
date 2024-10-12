from src.modules.delete_student_organization.app.delete_student_organization_viewmodel import DeleteStudentOrganizationViewmodel
from src.shared.domain.entities.student_organization import StudentOrganization


class Test_DeleteStudentOrganizationViewmodel:
    def test_delete_student_organization_viewmodel(self):
        stu_org = StudentOrganization(
            name="name",
            description="description",
            creation_date=1,
            logo="logo",
            instagram="instagram",
            website_link="website_link"
        )

        viewmodel = DeleteStudentOrganizationViewmodel(
            stu_org_id=stu_org.stu_org_id,
            name=stu_org.name,
            description=stu_org.description,
            creation_date=stu_org.creation_date,
            logo=stu_org.logo,
            instagram=stu_org.instagram,
            website_link=stu_org.website_link
        ).to_dict()

        expected = {
            "stu_org_id": stu_org.stu_org_id,
            "name": stu_org.name,
            "description": stu_org.description,
            "creation_date": stu_org.creation_date,
            "logo": stu_org.logo,
            "instagram": stu_org.instagram,
            "website_link": stu_org.website_link
        }	

        assert viewmodel == expected
