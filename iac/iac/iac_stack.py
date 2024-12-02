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
            "get-all-courses": self.lambda_stack.get_all_courses_function,
            "create-course": self.lambda_stack.create_course_function,
            "update-course": self.lambda_stack.update_course_function,
            "delete-course": self.lambda_stack.delete_course_function,
            "get-all-events": self.lambda_stack.get_all_events_function,
            "create-event": self.lambda_stack.create_event_function,
            "update-event": self.lambda_stack.update_event_function,
            "delete-event": self.lambda_stack.delete_event_function,
            "get-all-members": self.lambda_stack.get_all_members_function,
            "create-member": self.lambda_stack.create_member_function,
            "get-all-student-organizations": self.lambda_stack.get_all_student_organizations_function,
            "create-student-organization": self.lambda_stack.create_student_organization_function,
            "update-student-organization": self.lambda_stack.update_student_organization_function,
            "delete-student-organization": self.lambda_stack.delete_student_organization_function,
            "get-all-notifications": self.lambda_stack.get_all_student_organizations_function,
            "create-notification": self.lambda_stack.create_student_organization_function,
            "update-notification": self.lambda_stack.update_student_organization_function,
            "delete-notification": self.lambda_stack.delete_student_organization_function,
            "get-course": self.lambda_stack.get_course_function,
            "get-student-organization": self.lambda_stack.get_student_organization_function,
            "get-member": self.lambda_stack.get_member_function,
            "get-event": self.lambda_stack.get_event_function
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
