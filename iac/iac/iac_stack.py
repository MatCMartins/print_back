from aws_cdk import (
    Stack,
)
from constructs import Construct

from aws_cdk.aws_apigateway import RestApi, Cors
from aws_cdk.aws_iam import Role, ServicePrincipal, PolicyStatement

from .dynamo_stack import DynamoStack
from .bucket_stack import BucketStack
from .lambda_stack import LambdaStack


class IacStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.dynamo_stack = DynamoStack(self)
        self.bucket_stack = BucketStack(self)

        # API Gateway Config with OpenID Connect Integration
        self.rest_api = RestApi(
            self,
            "SemanaPrint_RestApi",
            rest_api_name="SemanaPrint_RestApi",
            description="Semana Print RestApi",
            default_cors_preflight_options={
                "allow_origins": Cors.ALL_ORIGINS,
                "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": Cors.DEFAULT_HEADERS,
            },
        )

        # Add Authorization with Azure AD (OpenID Connect)
        azure_ad_oidc = {
            "authorization_endpoint": "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize",
            "token_endpoint": "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token",
            "user_info_endpoint": "https://graph.microsoft.com/oidc/userinfo",
            "client_id": "{client_id}",
        }

        self.rest_api.root.add_method(
            "ANY",
            None,  # Integration will be set by LambdaStack
            authorization_type=None,  # Handle auth manually in Lambda
            api_key_required=False,
        )

        ENVIRONMENT_VARIABLES = {
            "STAGE": "TEST",
            "AZURE_AD_CLIENT_ID": "{client_id}",
            "AZURE_AD_TENANT_ID": "{tenant_id}",
            "DYNAMO_TABLE_COURSE": self.dynamo_stack.dynamo_table_course.table_name,
            "DYNAMO_TABLE_EVENT": self.dynamo_stack.dynamo_table_event.table_name,
            "DYNAMO_TABLE_MEMBER": self.dynamo_stack.dynamo_table_member.table_name,
            "DYNAMO_TABLE_STU_ORG": self.dynamo_stack.dynamo_table_student_org.table_name,
        }

        self.lambda_stack = LambdaStack(self, environment_variables=ENVIRONMENT_VARIABLES)

        # Grant DynamoDB permissions to Lambda functions
        for f in self.lambda_stack.functions_that_need_dynamo_permissions:
            self.dynamo_stack.dynamo_table_course.grant_read_write_data(f)
            self.dynamo_stack.dynamo_table_event.grant_read_write_data(f)
            self.dynamo_stack.dynamo_table_member.grant_read_write_data(f)
            self.dynamo_stack.dynamo_table_student_org.grant_read_write_data(f)
