import json
from dataclasses import dataclass
import pytest

from src.modules.get_student_organization.app.get_student_organization_presenter import lambda_handler
from src.shared.infra.repositories.student_organization_repository_mock import StudentOrganizationRepositoryMock

class Test_GetStudentOrganizationPresenter:

    def test_get_student_organization_presenter(self):
        first_org_id = StudentOrganizationRepositoryMock().stu_orgs[0].stu_org_id
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
                "stu_org_id": first_org_id
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
        assert json.loads(response["body"])["name"] == "Data Science Club IMT"
        assert json.loads(response["body"])["description"] == "Organization dedicated to promoting knowledge and projects in the field of data science and machine learning."
        assert json.loads(response["body"])["creation_date"] == 1620009600
        assert json.loads(response["body"])["logo"] == "https://datascienceclubimt.com/logo.png"
        assert json.loads(response["body"])["instagram"] == "https://instagram.com/datascienceclubimt"
        assert json.loads(response["body"])["website_link"] == "https://datascienceimt.com"