from src.modules.update_student_organization.app.update_student_organization_viewmodel import UpdateStudentOrganizationViewmodel
from src.shared.domain.entities.student_organization import StudentOrganization


class Test_UpdateStudentOrganizationViewmodel:
    def test_delete_student_organization_viewmodel(self):
        stu_org = StudentOrganization(
            stu_org_id="b9799d9d-798c-4f44-9fd7-b9ae41c77496",
            name="name",
            description="description",
            creation_date=1,
            logo="logo",
            instagram="instagram",
        )

        viewmodel = UpdateStudentOrganizationViewmodel(
            stu_org_id=stu_org.stu_org_id,
            name=stu_org.name,
            description=stu_org.description,
            creation_date=stu_org.creation_date,
            logo=stu_org.logo,
            instagram=stu_org.instagram,
        ).to_dict()

        expected = {
            "stu_org_id": stu_org.stu_org_id,
            "name": stu_org.name,
            "description": stu_org.description,
            "creation_date": stu_org.creation_date,
            "logo": stu_org.logo,
            "instagram": stu_org.instagram,
        }	

        assert viewmodel == expected
