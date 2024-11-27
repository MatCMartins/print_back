from aws_cdk import (
    aws_lambda as lambda_,
    Duration,
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration, CognitoUserPoolsAuthorizer


class LambdaStack(Construct):
    functions_that_need_dynamo_permissions = []
    functions_that_need_dynamo_member_permissions = []
    functions_that_need_ses_permissions = []
    functions_that_need_s3_permissions = []

    def __init__(self, scope: Construct, api_gateway_resource: Resource, environment_variables: dict, authorizer: CognitoUserPoolsAuthorizer) -> None:
        super().__init__(scope, "LambdaStack")

        # Criar Lambda Layer
        self.lambda_layer = lambda_.LayerVersion(
            self,
            "SharedLayer",
            code=lambda_.Code.from_asset("./lambda_layer_out_temp"),  # Ajustar path para sua camada
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_9],
        )

        # Funções Lambda e integração com API Gateway
        self.create_course_function = self.create_lambda_api_gateway_integration(
            "create_course", "POST", api_gateway_resource, environment_variables, authorizer
        )
        self.create_event_function = self.create_lambda_api_gateway_integration(
            "create_event", "POST", api_gateway_resource, environment_variables, authorizer
        )
        self.create_member_function = self.create_lambda_api_gateway_integration(
            "create_member", "POST", api_gateway_resource, environment_variables, authorizer
        )
        self.create_student_organization_function = self.create_lambda_api_gateway_integration(
            "create_student_organization", "POST", api_gateway_resource, environment_variables, authorizer
        )

        self.delete_course_function = self.create_lambda_api_gateway_integration(
            "delete_course", "DELETE", api_gateway_resource, environment_variables, authorizer
        )
        self.delete_event_function = self.create_lambda_api_gateway_integration(
            "delete_event", "DELETE", api_gateway_resource, environment_variables, authorizer
        )
        self.delete_student_organization_function = self.create_lambda_api_gateway_integration(
            "delete_student_organization", "DELETE", api_gateway_resource, environment_variables, authorizer
        )

        self.get_all_courses_function = self.create_lambda_api_gateway_integration(
            "get_all_courses", "GET", api_gateway_resource, environment_variables, authorizer
        )
        self.get_all_events_function = self.create_lambda_api_gateway_integration(
            "get_all_events", "GET", api_gateway_resource, environment_variables, authorizer
        )
        self.get_all_members_function = self.create_lambda_api_gateway_integration(
            "get_all_members", "GET", api_gateway_resource, environment_variables, authorizer
        )
        self.get_all_student_organizations_function = self.create_lambda_api_gateway_integration(
            "get_all_student_organizations", "GET", api_gateway_resource, environment_variables, authorizer
        )

        self.get_course_function = self.create_lambda_api_gateway_integration(
            "get_course", "GET", api_gateway_resource, environment_variables, authorizer
        )
        self.get_event_function = self.create_lambda_api_gateway_integration(
            "get_event", "GET", api_gateway_resource, environment_variables, authorizer
        )
        self.get_member_function = self.create_lambda_api_gateway_integration(
            "get_member", "GET", api_gateway_resource, environment_variables, authorizer
        )
        self.get_student_organization_function = self.create_lambda_api_gateway_integration(
            "get_student_organization", "GET", api_gateway_resource, environment_variables, authorizer
        )

        self.update_course_function = self.create_lambda_api_gateway_integration(
            "update_course", "PUT", api_gateway_resource, environment_variables, authorizer
        )
        self.update_event_function = self.create_lambda_api_gateway_integration(
            "update_event", "PUT", api_gateway_resource, environment_variables, authorizer
        )
        self.update_student_organization_function = self.create_lambda_api_gateway_integration(
            "update_student_organization", "PUT", api_gateway_resource, environment_variables, authorizer
        )

        # Categorizar permissões
        self.functions_that_need_dynamo_permissions = [
            self.create_course_function,
            self.delete_event_function,
            self.get_all_courses_function,
            self.update_event_function,
        ]

        self.functions_that_need_s3_permissions = [
            self.create_member_function,
            self.update_course_function,
        ]

        self.functions_that_need_ses_permissions = [
            self.update_event_function,
            self.update_student_organization_function,
        ]

    def create_lambda_api_gateway_integration(self, module_name: str, method: str, api_resource: Resource, environment_variables: dict, authorizer: CognitoUserPoolsAuthorizer):
        """
        Cria uma função Lambda integrada diretamente ao API Gateway com um método HTTP.
        """
        function = lambda_.Function(
            self,
            module_name.title(),
            code=lambda_.Code.from_asset(f"../src/modules/{module_name}"),
            handler=f"app.{module_name}_presenter.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer],  # Adiciona camada compartilhada
            environment=environment_variables,
            timeout=Duration.seconds(15),
        )

        # Adiciona integração ao API Gateway
        resource = api_resource.add_resource(module_name.replace("_", "-"))
        resource.add_method(method, LambdaIntegration(function), authorizer=authorizer)

        return function
