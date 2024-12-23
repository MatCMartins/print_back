import json
from unittest.mock import patch

from src.modules.create_member.app.create_member_presenter import lambda_handler

class Test_CreateMemberPresenter:
    @patch("src.modules.create_member.app.create_member_presenter.authenticate")
    def test_create_member_presenter(self, mock_authenticate):
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
                "member_id": "f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
                "name": "Mateus Martins",
                "email": "mateus.martins@gmail.com",
                "activities": []
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
        assert response["body"] == json.dumps({
            "member_id": "f1d6c8a7-3e9b-42c7-a123-9b8d2f4e5a1b",
            "name": "Mateus Martins",
            "email": "mateus.martins@gmail.com",
            "activities": []
        })

