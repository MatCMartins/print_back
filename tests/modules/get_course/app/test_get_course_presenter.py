import json
from unittest.mock import patch
from src.modules.get_course.app.get_course_presenter import lambda_handler
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock

repo = CourseRepositoryMock()

class Test_GetCoursePresenter:
    @patch("src.modules.get_course.app.get_course_presenter.authenticate")
    def test_get_course_presenter(self, mock_authenticate):
        mock_authenticate.return_value = "mock_token_valid"
        first_course_id = repo.courses[0].course_id
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/my/path",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "queryStringParameters": {
                "course_id": first_course_id
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                    "iam": {
                        "accessKey": "AKIA...",
                        "accountId": "111122223333",
                        "callerId": "AIDA...",
                        "cognitoIdentity": None,
                        "principalcourseId": None,
                        "userArn": "arn:aws:iam::111122223333:user/example-user",
                        "userId": "AIDA..."
                    }
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "external_interfaces": {
                    "method": "POST",
                    "path": "/my/path",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": "Hello from client!",
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        response_body = json.loads(response["body"])

        assert response["statusCode"] == 200
        assert response_body["course_id"] == first_course_id
        assert response_body["name"] == repo.courses[0].name
        assert response_body["description"] == repo.courses[0].description
        assert response_body["coordinator"] == repo.courses[0].coordinator
        assert response_body["link"] == repo.courses[0].link
        assert response_body["course_photo"] == repo.courses[0].course_photo
        assert response_body["coordinator_photo"] == repo.courses[0].coordinator_photo
        