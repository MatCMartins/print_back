from .get_student_organization_controller import GetStudentOrganizationController
from .get_student_organization_usecase import GetStudentOrganizationsUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


observability = Environments.get_observability()(module_name="get_user")

repo = Environments.get_user_repo()()
usecase = GetStudentOrganizationsUsecase(repo)
controller = GetStudentOrganizationController(usecase)

def lambda_handler(event, context):
    
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    response = httpResponse.toDict()
    
    return response