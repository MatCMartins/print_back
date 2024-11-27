from aws_cdk import (
    aws_lambda as lambda_,
    Duration,
)
from constructs import Construct


class LambdaStack(Construct):
    # Lista de funções que precisam de permissões específicas
    functions_that_need_dynamo_permissions = []

    def __init__(self, scope: Construct, environment_variables: dict) -> None:
        super().__init__(scope, "LambdaStack")

        # Criar todas as funções Lambda
        self.create_course_function = self.create_lambda_function("create_course", environment_variables)
        self.create_event_function = self.create_lambda_function("create_event", environment_variables)
        self.create_member_function = self.create_lambda_function("create_member", environment_variables)
        self.create_student_organization_function = self.create_lambda_function("create_student_organization", environment_variables)

        self.delete_course_function = self.create_lambda_function("delete_course", environment_variables)
        self.delete_event_function = self.create_lambda_function("delete_event", environment_variables)
        self.delete_student_organization_function = self.create_lambda_function("delete_student_organization", environment_variables)

        self.get_all_courses_function = self.create_lambda_function("get_all_courses", environment_variables)
        self.get_all_events_function = self.create_lambda_function("get_all_events", environment_variables)
        self.get_all_members_function = self.create_lambda_function("get_all_members", environment_variables)
        self.get_all_student_organizations_function = self.create_lambda_function("get_all_student_organizations", environment_variables)

        self.get_course_function = self.create_lambda_function("get_course", environment_variables)
        self.get_event_function = self.create_lambda_function("get_event", environment_variables)
        self.get_member_function = self.create_lambda_function("get_member", environment_variables)
        self.get_student_organization_function = self.create_lambda_function("get_student_organization", environment_variables)

        self.update_course_function = self.create_lambda_function("update_course", environment_variables)
        self.update_event_function = self.create_lambda_function("update_event", environment_variables)
        self.update_student_organization_function = self.create_lambda_function("update_student_organization", environment_variables)

        # Registrar funções que precisam de permissões para DynamoDB
        self.functions_that_need_dynamo_permissions = [
            self.create_course_function,
            self.create_event_function,
            self.create_member_function,
            self.create_student_organization_function,
            self.delete_course_function,
            self.delete_event_function,
            self.delete_student_organization_function,
            self.get_all_courses_function,
            self.get_all_events_function,
            self.get_all_members_function,
            self.get_all_student_organizations_function,
            self.get_course_function,
            self.get_event_function,
            self.get_member_function,
            self.get_student_organization_function,
            self.update_course_function,
            self.update_event_function,
            self.update_student_organization_function,
        ]

    def create_lambda_function(self, module_name: str, environment_variables: dict):
        """
        Cria uma função Lambda para um módulo específico.
        """
        return lambda_.Function(
            self,
            f"{module_name}_lambda",
            code=lambda_.Code.from_asset(f"../src/modules/{module_name}"),
            handler=f"{module_name}.handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            environment=environment_variables,
            timeout=Duration.seconds(15),
        )
