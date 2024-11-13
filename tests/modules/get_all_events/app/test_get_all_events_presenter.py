import json
from src.modules.get_all_events.app.get_all_events_presenter import lambda_handler
from src.shared.infra.repositories.event_repository_mock import EventRepositoryMock

class Test_GetAllEventsPresenter:

    def test_get_all_events_presenter(self):
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
        assert "events" in body
        events = body["events"]

        repo = EventRepositoryMock()
        assert isinstance(events, list)
        assert len(events) == len(repo.events)
        
        for i, event_data in enumerate(events):
            assert event_data["name"] == repo.events[i].name
            assert event_data["description"] == repo.events[i].description
            assert event_data["banner"] == repo.events[i].banner
            assert event_data["start_date"] == repo.events[i].start_date
            assert event_data["end_date"] == repo.events[i].end_date
            assert event_data["rooms"] == repo.events[i].rooms
            assert event_data["subscribers"] == repo.events[i].subscribers
