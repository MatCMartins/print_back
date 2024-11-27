from aws_cdk import (
    aws_lambda as lambda_,
    Duration,
)
from constructs import Construct


class LambdaStack(Construct):
    functions_that_need_dynamo_permissions = []

    def __init__(self, scope: Construct, environment_variables: dict) -> None:
        super().__init__(scope, "LambdaStack")

        self.create_course_function = self.create_lambda(
            "create_course", environment_variables
        )
        self.create_event_function = self.create_lambda(
            "create_event", environment_variables
        )
        self.create_member_function = self.create_lambda(
            "create_member", environment_variables
        )
        self.create_student_org_function = self.create_lambda(
            "create_student_organization", environment_variables
        )

        self.functions_that_need_dynamo_permissions = [
            self.create_course_function,
            self.create_event_function,
            self.create_member_function,
            self.create_student_org_function,
        ]

    def create_lambda(self, module_name: str, environment_variables: dict):
        return lambda_.Function(
            self,
            module_name,
            code=lambda_.Code.from_asset(f"../src/{module_name}"),
            handler=f"{module_name}.handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            environment=environment_variables,
            timeout=Duration.seconds(15),
        )
