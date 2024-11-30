import json
from unittest.mock import patch

from src.modules.get_all_courses.app.get_all_courses_presenter import lambda_handler
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock

class Test_GetAllCoursesPresenter:
    @patch("src.modules.get_all_courses.app.get_all_courses_presenter.authenticate")
    def test_get_all_courses_presenter(self, mock_authenticate):
        mock_authenticate.return_value = "mock_token_valid"
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
            "queryStringParameters": {},
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
                        "principalOrgId": None,
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
            "isBase64Encoded": False,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 200
        body = json.loads(response["body"])

        assert isinstance(body, dict)
        assert "courses" in body
        courses = body["courses"]

        repo = CourseRepositoryMock()
        assert isinstance(courses, list)
        assert len(courses) == len(repo.courses)
        
        for i, course_data in enumerate(courses):
            assert course_data["name"] == repo.courses[i].name
            assert course_data["course_photo"] == repo.courses[i].course_photo
            assert course_data["coordinator"] == repo.courses[i].coordinator
            assert course_data["coordinator_photo"] == repo.courses[i].coordinator_photo
            assert course_data["description"] == repo.courses[i].description
            assert course_data["link"] == repo.courses[i].link