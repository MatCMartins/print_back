import json
from src.modules.create_event.app.create_event_presenter import lambda_handler

class Test_CreateEventPresenter:

    def test_create_event_presenter(self):
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
                "name": "Tech Conference 2023",
                "description": "Annual tech conference",
                "banner": "banner_url",
                "start_date": 1672531200,
                "end_date": 1672617600,
                "rooms": {"Main Hall": 100, "Workshop Room 1": 30},
                "subscribers": {"user1": "Main Hall", "user2": "Workshop Room 1"}
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
        body = json.loads(response["body"])
        assert body["name"] == "Tech Conference 2023"
        assert body["description"] == "Annual tech conference"
        assert body["banner"] == "banner_url"
        assert body["start_date"] == 1672531200
        assert body["end_date"] == 1672617600
        assert body["rooms"] == {"Main Hall": 100, "Workshop Room 1": 30}
        assert body["subscribers"] == {"user1": "Main Hall", "user2": "Workshop Room 1"}