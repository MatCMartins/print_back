import os
from aws_cdk import Stack
from aws_cdk.aws_apigateway import RestApi, Cors, CfnAuthorizer, AuthorizationType
from constructs import Construct

from .dynamo_stack import DynamoStack
from .bucket_stack import BucketStack
from .lambda_stack import LambdaStack


class IacStack(Stack):
    lambda_stack: LambdaStack

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Obter Tenant ID e Client ID do Azure AD
        self.tenant_id = os.environ.get("AZURE_AD_TENANT_ID")
        self.client_id = os.environ.get("AZURE_AD_CLIENT_ID")
        self.github_ref_name = os.environ.get("GITHUB_REF_NAME")
        self.aws_region = os.environ.get("AWS_REGION")

        if not self.tenant_id or not self.client_id:
            raise ValueError("AZURE_AD_TENANT_ID and AZURE_AD_CLIENT_ID must be set in environment variables")

        # Configurar API Gateway
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

        api_gateway_resource = self.rest_api.root.add_resource(
            "mss-action",
            default_cors_preflight_options={
                "allow_origins": Cors.ALL_ORIGINS,
                "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": Cors.DEFAULT_HEADERS,
            },
        )

        # Configurar Lambda para autenticação via Azure AD
        validate_token_lambda = self.create_validate_token_lambda()

        # Configurar Authorizer com a Lambda
        azure_ad_authorizer = CfnAuthorizer(
            self,
            "AzureADLambdaAuthorizer",
            name="AzureAD_Lambda_Authorizer",
            type="REQUEST",
            rest_api_id=self.rest_api.rest_api_id,
            identity_source="method.request.header.Authorization",
            authorizer_uri=validate_token_lambda.function_arn,
        )

        # Associar o authorizer ao recurso da API
        api_gateway_resource.add_method(
            "GET",
            authorization_type=AuthorizationType.CUSTOM,
            authorizer=azure_ad_authorizer,
        )

        # Criar stacks auxiliares
        self.dynamo_stack = DynamoStack(self)
        self.bucket_stack = BucketStack(self)

        # Variáveis de ambiente para Lambdas
        ENVIRONMENT_VARIABLES = {
            "STAGE": self.github_ref_name.upper(),
            "AZURE_AD_CLIENT_ID": self.client_id,
            "AZURE_AD_TENANT_ID": self.tenant_id,
            "DYNAMO_TABLE_COURSE": self.dynamo_stack.dynamo_table_course.table_name,
            "DYNAMO_TABLE_EVENT": self.dynamo_stack.dynamo_table_event.table_name,
            "DYNAMO_TABLE_MEMBER": self.dynamo_stack.dynamo_table_member.table_name,
            "DYNAMO_TABLE_STU_ORG": self.dynamo_stack.dynamo_table_student_org.table_name,
            "REGION": self.aws_region,
            "S3_BUCKET_COURSE": self.bucket_stack.course_bucket.bucket_name,
            "S3_BUCKET_EVENT": self.bucket_stack.event_bucket.bucket_name,
            "S3_BUCKET_MEMBER": self.bucket_stack.member_bucket.bucket_name,
            "S3_BUCKET_STUDENT_ORG": self.bucket_stack.student_org_bucket.bucket_name,
        }

        # Criar stack Lambda
        self.lambda_stack = LambdaStack(
            self,
            environment_variables=ENVIRONMENT_VARIABLES,
        )

    def create_validate_token_lambda(self):
        """
        Cria a função Lambda para validar tokens JWT do Azure AD.
        """
        from aws_cdk.aws_lambda import Function, Runtime, Code

        return Function(
            self,
            "ValidateTokenLambda",
            runtime=Runtime.PYTHON_3_9,
            handler="validate_token.handler",
            code=Code.from_asset("src/validate_token"),
            environment={
                "AZURE_AD_CLIENT_ID": self.client_id,
                "AZURE_AD_TENANT_ID": self.tenant_id,
            },
        )
