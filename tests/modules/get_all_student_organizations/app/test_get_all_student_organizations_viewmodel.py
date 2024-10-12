from src.modules.get_all_student_organizations.app.get_all_student_organizations_viewmodel import GetAllStudentOrganizationsViewmodel
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock
 

class Test_GetStudentOrganizationViewmodel:
    def test_get_student_organization_viewmodel(self):
        stu_orgs = StudentOrganizationRepositoryMock().stu_orgs
        viewmodel = GetAllStudentOrganizationsViewmodel(stu_orgs).to_dict()
        expected = {"student_organizations":
            [
                {
                    "stu_org_id": stu_orgs[0].stu_org_id,
                    "name": "Data Science Club IMT",
                    "description": "Organization dedicated to promoting knowledge and projects in the field of data science and machine learning.",
                    "creation_date": 1620009600,
                    "logo": "https://datascienceclubimt.com/logo.png",
                    "instagram": "https://instagram.com/datascienceclubimt",
                    "website_link": "https://datascienceimt.com"
                },
                {
                    "stu_org_id": stu_orgs[1].stu_org_id,
                    "name": "AI Lab Mauá",
                    "description": "A community focused on artificial intelligence research and applications, encouraging students to participate in AI projects.",
                    "creation_date": 1609459200,
                    "logo": "https://ailabmaua.com/logo.png",
                    "instagram": "https://instagram.com/ailabmaua",
                    "website_link": "https://ailabmaua.com"
                },
                {
                    "stu_org_id": stu_orgs[2].stu_org_id,
                    "name": "Robotics Team Mauá",
                    "description": "A student organization focused on building and programming autonomous robots to compete in national and international competitions.",
                    "creation_date": 1619827200,
                    "logo": "https://roboticsteam.com/logo.png",
                    "instagram": "https://instagram.com/roboticsteammaua",
                    "website_link": "https://roboticsteammaua.com"
                }
            ]
        }

        assert viewmodel == expected
