from aws_cdk import (
    aws_lambda as lambda_,
    Duration,
)
from constructs import Construct


class LambdaStack(Construct):
    functions_that_need_dynamo_permissions = []
    functions_that_need_dynamo_member_permissions = []
    functions_that_need_ses_permissions = []
    functions_that_need_s3_permissions = []

    def __init__(self, scope: Construct, environment_variables: dict) -> None:
        super().__init__(scope, "LambdaStack")

        self.lambda_layer = lambda_.LayerVersion(self, "SemanaPrint_Layer",
                                                 code=lambda_.Code.from_asset("./lambda_layer_out_temp"),
                                                 compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                 )

        self.create_course_function = self.create_lambda_function("create_course", environment_variables)
        self.create_event_function = self.create_lambda_function("create_event", environment_variables)
        self.create_member_function = self.create_lambda_function("create_member", environment_variables)
        self.create_student_organization_function = self.create_lambda_function("create_student_organization", environment_variables)
        self.create_notification_function = self.create_lambda_function("create_notification", environment_variables)

        self.delete_course_function = self.create_lambda_function("delete_course", environment_variables)
        self.delete_event_function = self.create_lambda_function("delete_event", environment_variables)
        self.delete_student_organization_function = self.create_lambda_function("delete_student_organization", environment_variables)
        self.delete_notification_function = self.create_lambda_function("delete_notification", environment_variables)

        self.get_all_courses_function = self.create_lambda_function("get_all_courses", environment_variables)
        self.get_all_events_function = self.create_lambda_function("get_all_events", environment_variables)
        self.get_all_members_function = self.create_lambda_function("get_all_members", environment_variables)
        self.get_all_student_organizations_function = self.create_lambda_function("get_all_student_organizations", environment_variables)
        self.get_all_notifications_function = self.create_lambda_function("get_all_notifications", environment_variables)

        self.get_course_function = self.create_lambda_function("get_course", environment_variables)
        self.get_event_function = self.create_lambda_function("get_event", environment_variables)
        self.get_member_function = self.create_lambda_function("get_member", environment_variables)
        self.get_student_organization_function = self.create_lambda_function("get_student_organization", environment_variables)
        self.get_notification_function = self.create_lambda_function("get_notification", environment_variables)

        self.update_course_function = self.create_lambda_function("update_course", environment_variables)
        self.update_event_function = self.create_lambda_function("update_event", environment_variables)
        self.update_student_organization_function = self.create_lambda_function("update_student_organization", environment_variables)
        self.update_notification_function = self.create_lambda_function("update_notification", environment_variables)

        self.functions_that_need_dynamo_permissions = [
            self.create_course_function,
            self.create_event_function,
            self.create_member_function,
            self.create_student_organization_function,
            self.create_notification_function,
            self.delete_course_function,
            self.delete_event_function,
            self.delete_student_organization_function,
            self.delete_notification_function,
            self.get_all_courses_function,
            self.get_all_events_function,
            self.get_all_members_function,
            self.get_all_student_organizations_function,
            self.get_all_notifications_function,
            self.get_course_function,
            self.get_event_function,
            self.get_member_function,
            self.get_student_organization_function,
            self.get_notification_function,
            self.update_course_function,
            self.update_event_function,
            self.update_student_organization_function,
            self.update_notification_function,
        ]

        self.functions_that_need_s3_permissions = [
            self.create_member_function,
            self.update_course_function,
            self.create_student_organization_function,
            self.create_notification_function,
        ]

        self.functions_that_need_ses_permissions = [
            self.update_event_function,
            self.update_student_organization_function,
            self.update_notification_function,
        ]

        self.functions_that_need_dynamo_member_permissions = [
            self.get_member_function,
            self.get_all_members_function,
            self.create_member_function,
        ]

    def create_lambda_function(self, module_name: str, environment_variables: dict):
        """
        Cria uma função Lambda para um módulo específico, seguindo o padrão de handler "app.{module_name}_presenter.lambda_handler".
        """
        return lambda_.Function(
            self,
            f"{module_name}_lambda",
            code=lambda_.Code.from_asset(f"../src/modules/{module_name}"),
            handler=f"app.{module_name}_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer],
            environment=environment_variables,
            timeout=Duration.seconds(15),
        )
