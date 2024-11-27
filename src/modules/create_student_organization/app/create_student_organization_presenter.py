from .create_student_organization_controller import CreateStudentOrganizationController
from .create_student_organization_usecase import CreateStudentOrganizationUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_student_org_repo()
usecase = CreateStudentOrganizationUsecase(repo)
controller = CreateStudentOrganizationController(usecase)

def lambda_handler(event, context):
    
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    response = httpResponse.toDict()
    
    return response