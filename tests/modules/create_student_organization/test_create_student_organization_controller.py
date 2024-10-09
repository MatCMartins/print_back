from src.modules.create_student_organization.app.create_student_organization_controller import CreateStudentOrganizationController
from src.modules.create_student_organization.app.create_student_organization_usecase import CreateStudentOrganizationUsecase
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest

repo = StudentOrganizationRepositoryMock()

class Test_CreateStudentOrganizatiosController:
    def test_create_student_organization_controller(self):
        usecase = CreateStudentOrganizationUsecase(repo)
        controller = CreateStudentOrganizationController(usecase)

        request = HttpRequest(query_params={
            "name": "Data Science Club IMT",
            "description": "Data Science Club IMT",
            "creation_date": 234567890,
            "logo": "logo",
            "instagram": "instagram",
            "website_link": "website_link"
        })

        response = controller(request)

        assert response.status_code == 201
        assert response.body["name"] == "Data Science Club IMT"
        assert response.body["description"] == "Data Science Club IMT"
        assert response.body["creation_date"] == 234567890
        assert response.body["logo"] == "logo"
        assert response.body["instagram"] == "instagram"
        assert response.body["website_link"] == "website_link"
    
    def test_create_student_organization_controller_misssing_name(self):
        usecase = CreateStudentOrganizationUsecase(repo)
        controller = CreateStudentOrganizationController(usecase)

        request = HttpRequest(query_params={
            "description": "Data Science Club IMT",
            "creation_date": 234567890,
            "logo": "logo",
            "instagram": "instagram",
            "website_link": "website_link"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field name is missing"
    
    def test_create_student_organization_controller_misssing_description(self):
        usecase = CreateStudentOrganizationUsecase(repo)
        controller = CreateStudentOrganizationController(usecase)

        request = HttpRequest(query_params={
            "name": "Data Science Club IMT",
            "creation_date": 234567890,
            "logo": "logo",
            "instagram": "instagram",
            "website_link": "website_link"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field description is missing"
    
    def test_create_student_organization_controller_misssing_creation_date(self):
        usecase = CreateStudentOrganizationUsecase(repo)
        controller = CreateStudentOrganizationController(usecase)

        request = HttpRequest(query_params={
            "name": "Data Science Club IMT",
            "description": "Data Science Club IMT",
            "logo": "logo",
            "instagram": "instagram",
            "website_link": "website_link"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field creation_date is missing"

    def test_create_student_organization_controller_misssing_logo(self):
        usecase = CreateStudentOrganizationUsecase(repo)
        controller = CreateStudentOrganizationController(usecase)

        request = HttpRequest(query_params={
            "name": "Data Science Club IMT",
            "description": "Data Science Club IMT",
            "creation_date": 234567890,
            "instagram": "instagram",
            "website_link": "website_link"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field logo is missing"
    
    def test_create_student_organization_controller_misssing_instagram(self):
        usecase = CreateStudentOrganizationUsecase(repo)
        controller = CreateStudentOrganizationController(usecase)

        request = HttpRequest(query_params={
            "name": "Data Science Club IMT",
            "description": "Data Science Club IMT",
            "creation_date": 234567890,
            "logo": "logo",
            "website_link": "website_link"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field instagram is missing"

    def test_create_student_organization_controller_misssing_website_link(self):
        usecase = CreateStudentOrganizationUsecase(repo)
        controller = CreateStudentOrganizationController(usecase)

        request = HttpRequest(query_params={
            "name": "Data Science Club IMT",
            "description": "Data Science Club IMT",
            "creation_date": 234567890,
            "logo": "logo",
            "instagram": "instagram"
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field website_link is missing"
    