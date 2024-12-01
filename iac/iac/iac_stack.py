import os
from aws_cdk import (
    Stack,
    aws_iam,
)
from constructs import Construct
from aws_cdk.aws_apigateway import RestApi, Cors, LambdaIntegration

from .dynamo_stack import DynamoStack
from .bucket_stack import BucketStack
from .lambda_stack import LambdaStack


class IacStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.github_ref_name = os.environ.get("GITHUB_REF_NAME", "main")
        self.aws_region = os.environ.get("AWS_REGION", "sa-east-1")

        self.rest_api = RestApi(
            self,
            "ApiGateway",
            rest_api_name="ApplicationAPI",
            description="API Gateway for the Application",
            default_cors_preflight_options={
                "allow_origins": Cors.ALL_ORIGINS,
                "allow_methods": ["GET", "POST", "OPTIONS"],
                "allow_headers": Cors.DEFAULT_HEADERS,
            },
        )
        self.dynamo_stack = DynamoStack(self)
        self.bucket_stack = BucketStack(self)

        ENVIRONMENT_VARIABLES = {
            "STAGE": "PROD",
            "REGION": self.aws_region,
            "DYNAMO_COURSE_TABLE": self.dynamo_stack.dynamo_table_course.table_name,
            "DYNAMO_EVENT_TABLE": self.dynamo_stack.dynamo_table_event.table_name,
            "DYNAMO_MEMBER_TABLE": self.dynamo_stack.dynamo_table_member.table_name,
            "DYNAMO_STUDENT_ORG_TABLE": self.dynamo_stack.dynamo_table_student_org.table_name,
            "DYNAMO_NOTIFICATION_TABLE": self.dynamo_stack.dynamo_table_notification.table_name,
            "COURSE_BUCKET_NAME": self.bucket_stack.course_bucket.bucket_name,
            "EVENT_BUCKET_NAME": self.bucket_stack.event_bucket.bucket_name,
            "MEMBER_BUCKET_NAME": self.bucket_stack.member_bucket.bucket_name,
            "STUDENT_ORG_BUCKET_NAME": self.bucket_stack.student_org_bucket.bucket_name,
            "STUDENT_NOTIFICATION_NAME": self.bucket_stack.notification_bucket.bucket_name,
        }

        self.lambda_stack = LambdaStack(self, environment_variables=ENVIRONMENT_VARIABLES)

        self.add_individual_endpoints()

        self.grant_permissions()

    def add_individual_endpoints(self):

        endpoints = {
            "courses/get-all": self.lambda_stack.get_all_courses_function,
            "courses/create": self.lambda_stack.create_course_function,
            "courses/update": self.lambda_stack.update_course_function,
            "courses/delete": self.lambda_stack.delete_course_function,
            "events/get-all": self.lambda_stack.get_all_events_function,
            "events/create": self.lambda_stack.create_event_function,
            "events/update": self.lambda_stack.update_event_function,
            "events/delete": self.lambda_stack.delete_event_function,
            "members/get-all": self.lambda_stack.get_all_members_function,
            "members/create": self.lambda_stack.create_member_function,
            "student-organizations/get-all": self.lambda_stack.get_all_student_organizations_function,
            "student-organizations/create": self.lambda_stack.create_student_organization_function,
            "student-organizations/update": self.lambda_stack.update_student_organization_function,
            "student-organizations/delete": self.lambda_stack.delete_student_organization_function,
            "notifications/get-all": self.lambda_stack.get_all_student_organizations_function,
            "notifications/create": self.lambda_stack.create_student_organization_function,
            "notifications/update": self.lambda_stack.update_student_organization_function,
            "notifications/delete": self.lambda_stack.delete_student_organization_function,
            "course/get": self.lambda_stack.get_course_function,
            "student-organization/get": self.lambda_stack.get_student_organization_function,
            "member/get": self.lambda_stack.get_member_function,
            "event/get": self.lambda_stack.get_event_function,
        }

        for path, lambda_function in endpoints.items():
            api_resource = self.rest_api.root.add_resource(path)
            method = "GET" if "get-all" in path else "POST" 
            lambda_integration = LambdaIntegration(lambda_function)
            api_resource.add_method(method, lambda_integration)

    def grant_permissions(self):
        """
        Grant required DynamoDB and S3 permissions to Lambda functions.
        """
        for function in self.lambda_stack.functions_that_need_dynamo_permissions:
            self.dynamo_stack.dynamo_table_course.grant_read_write_data(function)
            self.dynamo_stack.dynamo_table_event.grant_read_write_data(function)
            self.dynamo_stack.dynamo_table_member.grant_read_write_data(function)
            self.dynamo_stack.dynamo_table_student_org.grant_read_write_data(function)
            self.dynamo_stack.dynamo_table_notification.grant_read_write_data(function)

        s3_admin_policy = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=["s3:*"],
            resources=["*"],
        )

        for function in self.lambda_stack.functions_that_need_dynamo_permissions:
            function.add_to_role_policy(s3_admin_policy)
