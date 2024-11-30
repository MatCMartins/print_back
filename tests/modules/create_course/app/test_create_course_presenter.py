import json
from unittest.mock import patch

from src.modules.create_course.app.create_course_presenter import lambda_handler

class Test_CreateCoursePresenter:
    @patch("src.modules.create_course.app.create_course_presenter.authenticate")
    def test_create_course_presenter(self, mock_authenticate):
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
            "queryStringParameters": {
                "name": "Physics",
                "description": "A course focused on physics.",
                "course_photo": "https://example.com/physics_photo.jpg",
                "coordinator": "John Doe",
                "coordinator_photo": "https://example.com/john_photo.jpg",
                "link": "https://example.com/physics"
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
            "isBase64Encoded": None,
            "stageVariables": None
        }
        response = lambda_handler(event, None)
        print(response)
        assert response["statusCode"] == 201
        assert json.loads(response["body"])["name"] == "Physics"
        assert json.loads(response["body"])["description"] == "A course focused on physics."
        assert json.loads(response["body"])["course_photo"] == "https://example.com/physics_photo.jpg"
        assert json.loads(response["body"])["coordinator"] == "John Doe"
        assert json.loads(response["body"])["coordinator_photo"] == "https://example.com/john_photo.jpg"
        assert json.loads(response["body"])["link"] == "https://example.com/physics"


