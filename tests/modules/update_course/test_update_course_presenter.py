import json
from dataclasses import dataclass
import pytest

from src.modules.update_course.app.update_course_presenter import lambda_handler
from src.shared.infra.repositories.course_repository_mock import CourseRepositoryMock

class Test_UpdateCoursePresenter:

    def test_update_course_presenter(self):
        first_course_id = CourseRepositoryMock().courses[0].course_id
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
                "course_id": first_course_id,
                "name": "Mathematics",
                "course_photo": "photo",
                "coordinator": "coordinator",
                "coordinator_photo": "photo",
                "description": "description",
                "link": "link"
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

        assert response["statusCode"] == 200
        assert json.loads(response["body"])["course_id"] == first_course_id
        assert json.loads(response["body"])["name"] == "Mathematics"
        assert json.loads(response["body"])["course_photo"] == "photo"
        assert json.loads(response["body"])["coordinator"] == "coordinator"
        assert json.loads(response["body"])["coordinator_photo"] == "photo"
        assert json.loads(response["body"])["description"] == "description"
        assert json.loads(response["body"])["link"] == "link"