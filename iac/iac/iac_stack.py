from aws_cdk import Stack
from aws_cdk.aws_apigateway import RestApi, Cors, TokenAuthorizer
from constructs import Construct
import os


class IacStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        tenant_id = os.environ.get("AZURE_AD_TENANT_ID")
        client_id = os.environ.get("AZURE_AD_CLIENT_ID")

        if not tenant_id or not client_id:
            raise ValueError("AZURE_AD_TENANT_ID and AZURE_AD_CLIENT_ID must be provided!")

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

        self.azure_ad_authorizer = TokenAuthorizer(
            self,
            "AzureADAuthorizer",
            handler=self.create_validation_lambda(client_id, tenant_id),
            identity_source="method.request.header.Authorization",
        )

    def create_validation_lambda(self, client_id: str, tenant_id: str):
        """
        Cria uma função Lambda para validar o token JWT do Azure AD.
        """
        from aws_cdk import aws_lambda as lambda_

        return lambda_.Function(
            self,
            "ValidateTokenLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="validate_token.handler",
            code=lambda_.Code.from_asset("src/validate_token"),
            environment={
                "AZURE_AD_CLIENT_ID": client_id,
                "AZURE_AD_TENANT_ID": tenant_id,
            },
        )
