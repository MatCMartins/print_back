import json
from unittest.mock import patch
from src.modules.get_member.app.get_member_presenter import lambda_handler
from src.shared.infra.repositories.member_repository_mock import MemberRepositoryMock

repo = MemberRepositoryMock()

class Test_GetMemberPresenter:
    @patch("src.modules.get_member.app.get_member_presenter.authenticate")
    def test_get_member_presenter(self, mock_authenticate):
        mock_authenticate.return_value = "mock_token_valid"
        first_member_id = repo.members[0].member_id
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
                "member_id": first_member_id
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

        print(response_body)
        assert response["statusCode"] == 200
        assert response_body["member_id"] == first_member_id
        assert response_body["name"] == repo.members[0].name
        assert response_body["email"] == repo.members[0].email
        assert response_body["activities"] == repo.members[0].activities
