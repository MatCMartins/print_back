from src.modules.update_student_organization.app.update_student_organization_controller import UpdateStudentOrganizationController
from src.modules.update_student_organization.app.update_student_organization_usecase import UpdateStudentOrganizationUsecase
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

class Test_UpdateStudentOrganizationController:
    def test_update_student_organization_controller(self):
        repo = StudentOrganizationRepositoryMock()
        usecase = UpdateStudentOrganizationUsecase(repo)
        controller = UpdateStudentOrganizationController(usecase)

        response = HttpRequest(query_params={
            "stu_org_id": repo.stu_orgs[0].stu_org_id,
            "name": "Maua Jr",
            "description": "This student organization is a junior company",
            "creation_date": 234567890,
            "logo": "logo",
            "instagram": "instagram",
            "website_link": "website_link"
        })

        response = controller(response)

        assert response.status_code == 200
        assert repo.stu_orgs[0].name == "Maua Jr"
        assert repo.stu_orgs[0].description == "This student organization is a junior company"
        assert repo.stu_orgs[0].creation_date == 234567890
        assert repo.stu_orgs[0].logo == "logo"
        assert repo.stu_orgs[0].instagram == "instagram"
        assert repo.stu_orgs[0].website_link == "website_link"
    
    def test_update_student_organization_no_stu_org_id(self):
        repo = StudentOrganizationRepositoryMock()
        usecase = UpdateStudentOrganizationUsecase(repo)
        controller = UpdateStudentOrganizationController(usecase)

        response = HttpRequest(query_params={
            "name": "Maua Jr",
            "description": "This student organization is a junior company",
            "creation_date": 234567890,
            "logo": "logo",
            "instagram": "instagram",
            "website_link": "website_link"
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field stu_org_id is missing"
    
    def test_update_student_organization_wrong_name_type(self):
        repo = StudentOrganizationRepositoryMock()
        usecase = UpdateStudentOrganizationUsecase(repo)
        controller = UpdateStudentOrganizationController(usecase)

        response = HttpRequest(query_params={
            "stu_org_id": repo.stu_orgs[0].stu_org_id,
            "name": 123,
            "description": "This student organization is a junior company",
            "creation_date": 234567890,
            "logo": "logo",
            "instagram": "instagram",
            "website_link": "website_link"
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field name isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
    
    def test_update_student_organization_wrong_description_type(self):
        repo = StudentOrganizationRepositoryMock()
        usecase = UpdateStudentOrganizationUsecase(repo)
        controller = UpdateStudentOrganizationController(usecase)

        response = HttpRequest(query_params={
            "stu_org_id": repo.stu_orgs[0].stu_org_id,
            "name": "Maua Jr",
            "description": 123,
            "creation_date": 234567890,
            "logo": "logo",
            "instagram": "instagram",
            "website_link": "website_link"
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field description isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"

    def test_update_student_organization_wrong_creation_date_type(self):
        repo = StudentOrganizationRepositoryMock()
        usecase = UpdateStudentOrganizationUsecase(repo)
        controller = UpdateStudentOrganizationController(usecase)

        response = HttpRequest(query_params={
            "stu_org_id": repo.stu_orgs[0].stu_org_id,
            "name": "Maua Jr",
            "description": "This student organization is a junior company",
            "creation_date": "234567890",
            "logo": "logo",
            "instagram": "instagram",
            "website_link": "website_link"
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field creation_date isn't the right type.\n Received: <class 'str'>.\n Expected: <class 'int'>"
    
    def test_update_student_organization_wrong_logo_type(self):
        repo = StudentOrganizationRepositoryMock()
        usecase = UpdateStudentOrganizationUsecase(repo)
        controller = UpdateStudentOrganizationController(usecase)

        response = HttpRequest(query_params={
            "stu_org_id": repo.stu_orgs[0].stu_org_id,
            "name": "Maua Jr",
            "description": "This student organization is a junior company",
            "creation_date": 234567890,
            "logo": 123,
            "instagram": "instagram",
            "website_link": "website_link"
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field logo isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
    
    def test_update_student_organization_wrong_instagram_type(self):
        repo = StudentOrganizationRepositoryMock()
        usecase = UpdateStudentOrganizationUsecase(repo)
        controller = UpdateStudentOrganizationController(usecase)

        response = HttpRequest(query_params={
            "stu_org_id": repo.stu_orgs[0].stu_org_id,
            "name": "Maua Jr",
            "description": "This student organization is a junior company",
            "creation_date": 234567890,
            "logo": "logo",
            "instagram": 123,
            "website_link": "website_link"
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field instagram isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
    
    def test_update_student_organization_wrong_website_link_type(self):
        repo = StudentOrganizationRepositoryMock()
        usecase = UpdateStudentOrganizationUsecase(repo)
        controller = UpdateStudentOrganizationController(usecase)

        response = HttpRequest(query_params={
            "stu_org_id": repo.stu_orgs[0].stu_org_id,
            "name": "Maua Jr",
            "description": "This student organization is a junior company",
            "creation_date": 234567890,
            "logo": "logo",
            "instagram": "instagram",
            "website_link": 123
        })

        response = controller(response)

        assert response.status_code == 400
        assert response.body == "Field website_link isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"