from .get_all_courses_controller import GetAllCoursesController
from .get_all_courses_usecase import GetAllCoursesUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.shared.helpers.auth import authenticate

repo = Environments.get_course_repo()
usecase = GetAllCoursesUsecase(repo)
controller = GetAllCoursesController(usecase)

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