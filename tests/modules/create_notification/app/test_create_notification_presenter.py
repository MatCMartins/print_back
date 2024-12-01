import json
from unittest.mock import patch

from src.modules.create_notification.app.create_notification_presenter import lambda_handler

class Test_CreateNotificationPresenter:
    @patch("src.modules.create_notification.app.create_notification_presenter.authenticate")
    def test_create_notification_presenter(self, mock_authenticate):
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
                "title": "Notification",
                "description": "Notification Description",
                "creation_date": 1234567890,
                "has_seen": ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]
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
        assert response["statusCode"] == 201
        assert json.loads(response["body"])["title"] == "Notification"
        assert json.loads(response["body"])["description"] == "Notification Description"
        assert json.loads(response["body"])["creation_date"] == 1234567890
        assert json.loads(response["body"])["has_seen"] == ["b9799d9d-798c-4f44-9fd7-b9ae41c77496"]

