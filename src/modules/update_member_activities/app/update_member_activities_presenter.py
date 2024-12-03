from .update_member_activities_usecase  import UpdateMemberActivitiesUsecase
from .update_member_activities_controller import UpdateMemberActivitiesController
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.shared.helpers.auth import authenticate

repo_member = Environments.get_member_repo()
repo_event = Environments.get_event_repo()
usecase = UpdateMemberActivitiesUsecase(repo_member, repo_event)
controller = UpdateMemberActivitiesController(usecase)

def lambda_handler(event, context):
    token = authenticate(event)
    if token:
        httpRequest = LambdaHttpRequest(data=event)
        response = controller(httpRequest)
        httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
        return httpResponse.toDict()
    else:
        return {
            "statusCode": 401,
            "body": "Unauthorized"
        }