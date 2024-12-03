import json
from dataclasses import dataclass
from unittest.mock import patch

from src.modules.update_member_activities.app.update_member_activities_presenter import lambda_handler
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

class Test_UpdateEventPresenter:
    @patch("src.modules.update_member_activities.app.update_member_activities_presenter.authenticate")
    def test_update_member_activities_presenter(self, mock_authenticate):
        mock_authenticate.return_value = "mock_token_valid"
        first_event_id = EventRepositoryMock().events[0].event_id
        first_member_id = MemberRepositoryMock().members[0].member_id
        activities = MemberRepositoryMock().members[2].activities
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
                "event_id": first_event_id,
                "member_id": first_member_id,
                "activities": activities
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
        assert response["statusCode"] == 200
        assert json.loads(response["body"])["member_id"] == first_member_id
        assert json.loads(response["body"])["activities"] == activities