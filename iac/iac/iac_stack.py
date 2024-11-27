import os
from aws_cdk import (
    Stack,
    aws_iam,
)
from constructs import Construct
from aws_cdk.aws_apigateway import RestApi, Cors

from .dynamo_stack import DynamoStack
from .bucket_stack import BucketStack
from .lambda_stack import LambdaStack


class IacStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Obtenção de variáveis de ambiente
        self.github_ref_name = os.environ.get("GITHUB_REF_NAME", "dev")
        self.aws_region = os.environ.get("AWS_REGION", "us-east-1")

        # Configuração da RestApi com CORS
        self.rest_api = RestApi(
            self,
            "ApiGateway",
            rest_api_name="ApplicationAPI",
            description="API Gateway for the Application",
            default_cors_preflight_options={
                "allow_origins": Cors.ALL_ORIGINS,
                "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": Cors.DEFAULT_HEADERS,
            },
        )

        # Adicionando o recurso principal
        api_gateway_resource = self.rest_api.root.add_resource(
            "api",
            default_cors_preflight_options={
                "allow_origins": Cors.ALL_ORIGINS,
                "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": Cors.DEFAULT_HEADERS,
            },
        )

        # Inicializando DynamoDB Stack
        self.dynamo_stack = DynamoStack(self)

        # Inicializando Bucket Stack
        self.bucket_stack = BucketStack(self)

        # Variáveis de ambiente para funções Lambda
        ENVIRONMENT_VARIABLES = {
            "STAGE": self.github_ref_name.upper(),
            "REGION": self.aws_region,
            "DYNAMO_COURSE_TABLE": self.dynamo_stack.dynamo_table_course.table_name,
            "DYNAMO_EVENT_TABLE": self.dynamo_stack.dynamo_table_event.table_name,
            "DYNAMO_MEMBER_TABLE": self.dynamo_stack.dynamo_table_member.table_name,
            "DYNAMO_STUDENT_ORG_TABLE": self.dynamo_stack.dynamo_table_student_org.table_name,
            "COURSE_BUCKET_NAME": self.bucket_stack.course_bucket.bucket_name,
            "EVENT_BUCKET_NAME": self.bucket_stack.event_bucket.bucket_name,
            "MEMBER_BUCKET_NAME": self.bucket_stack.member_bucket.bucket_name,
            "STUDENT_ORG_BUCKET_NAME": self.bucket_stack.student_org_bucket.bucket_name,
        }

        # Inicializando Lambda Stack
        self.lambda_stack = LambdaStack(
            self, environment_variables=ENVIRONMENT_VARIABLES
        )

        # Permissões para DynamoDB
        for function in self.lambda_stack.functions_that_need_dynamo_permissions:
            self.dynamo_stack.dynamo_table_course.grant_read_write_data(function)
            self.dynamo_stack.dynamo_table_event.grant_read_write_data(function)
            self.dynamo_stack.dynamo_table_member.grant_read_write_data(function)
            self.dynamo_stack.dynamo_table_student_org.grant_read_write_data(function)

        # Permissões para S3
        s3_admin_policy = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=["s3:*"],
            resources=["*"],
        )

        for function in self.lambda_stack.functions_that_need_dynamo_permissions:
            function.add_to_role_policy(s3_admin_policy)