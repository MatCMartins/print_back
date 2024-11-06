import json
from dataclasses import dataclass
import pytest

from src.modules.get_all_courses.app.get_all_courses_presenter import lambda_handler

class Test_GetAllCoursesPresenter:

    def test_get_all_courses_presenter(self):
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
        assert response["body"] == json.dumps({"courses": [{"course_id": "8329f5105520a1b72d062628c077ddfa", "name": "Computer Science", "course_photo": "https://example.com/computer_science_photo.jpg", "coordinator": "Alice Johnson", "coordinator_photo": "https://example.com/alice_photo.jpg", "description": "A course focused on programming, algorithms, and systems.", "link": "https://example.com/computer_science"}, {"course_id": "e19e98a669ae21f94ffd1659998fd072", "name": "Data Analytics", "course_photo": "https://example.com/data_analytics_photo.jpg", "coordinator": "Bob Smith", "coordinator_photo": "https://example.com/bob_photo.jpg", "description": "Learn how to analyze data and extract meaningful insights.", "link": "https://example.com/data_analytics"}, {"course_id": "7cb15e416d62919b1b40298324fbe30b", "name": "Marketing", "course_photo": "https://example.com/marketing_photo.jpg", "coordinator": "Carla Williams", "coordinator_photo": "https://example.com/carla_photo.jpg", "description": "Explore strategies for product promotion and brand management.", "link": None}]})
        
