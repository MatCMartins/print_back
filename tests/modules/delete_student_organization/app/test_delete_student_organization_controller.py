from src.modules.delete_student_organization.app.delete_student_organization_controller import DeleteStudentOrganizationController
from src.modules.delete_student_organization.app.delete_student_organization_usecase import DeleteStudentOrganizationsUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock

repo = StudentOrganizationRepositoryMock()

class Test_deleteStudentOrganizationController:
    def test_delete_student_organization_controller(self):
        usecase = DeleteStudentOrganizationsUsecase(repo)
        controller = DeleteStudentOrganizationController(usecase)

        request = HttpRequest(query_params={"stu_org_id": repo.stu_orgs[0].stu_org_id})

        response = controller(request)

        assert response.status_code == 200
        assert repo.stu_orgs[0].name == "AI Lab Mauá"
        assert repo.stu_orgs[0].description == "A community focused on artificial intelligence research and applications, encouraging students to participate in AI projects."
        assert repo.stu_orgs[0].creation_date == 1609459200
        assert repo.stu_orgs[0].logo == "https://ailabmaua.com/logo.png"
        assert repo.stu_orgs[0].instagram == "https://instagram.com/ailabmaua"

    def test_delete_student_organization_controller_no_items_found(self):
        usecase = DeleteStudentOrganizationsUsecase(repo)
        controller = DeleteStudentOrganizationController(usecase)

        request = HttpRequest(query_params={"stu_org_id": "12321"})

        response = controller(request)
    
        assert response.status_code == 400
        assert response.body == "No items found for Student Organization"
    
    def test_delete_student_organization_controller_wrong_parameter_type(self):
        usecase = DeleteStudentOrganizationsUsecase(repo)
        controller = DeleteStudentOrganizationController(usecase)

        request = HttpRequest(query_params={"stu_org_id": 1231})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field stu_org_id isn't the right type.\n Received: <class 'int'>.\n Expected: <class 'str'>"
        
    def test_delete_student_organization_controller_missing_parameter(self):
        usecase = DeleteStudentOrganizationsUsecase(repo)
        controller = DeleteStudentOrganizationController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request)
        assert response.status_code == 400
        assert response.body == "Field stu_org_id is missing"