from aws_cdk import Stack
from constructs import Construct
from aws_cdk.aws_apigateway import RestApi, Cors, CfnAuthorizer
from .dynamo_stack import DynamoStack
from .bucket_stack import BucketStack
from .lambda_stack import LambdaStack


class IacStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.dynamo_stack = DynamoStack(self)
        self.bucket_stack = BucketStack(self)

        self.rest_api = RestApi(
            self,
            "SemanaPrint_RestApi",
            rest_api_name="SemanaPrint_RestApi",
            description="Semana Print RestApi",
            default_cors_preflight_options={
                "allow_origins": Cors.ALL_ORIGINS,
                "allow_methods": Cors.ALL_METHODS,
                "allow_headers": Cors.DEFAULT_HEADERS,
            },
        )

        azure_ad_oidc_provider_arn = f"arn:aws:apigateway:{Stack.of(self).region}:oidc-provider/login.microsoftonline.com"

        self.azure_ad_authorizer = CfnAuthorizer(
            self,
            "AzureADAuthorizer",
            name="AzureAD_OIDC",
            rest_api_id=self.rest_api.rest_api_id,
            type="JWT",
            identity_source="method.request.header.Authorization",
            provider_arns=[azure_ad_oidc_provider_arn],
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
