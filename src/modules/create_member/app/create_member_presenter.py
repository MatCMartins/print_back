from .create_member_controller import CreateMemberController
from .create_member_usecase import CreateMemberUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_member_repo()
usecase = CreateMemberUsecase(repo)
controller = CreateMemberController(usecase)

def lambda_handler(event, context):
    
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    response = httpResponse.toDict()
    
    return response