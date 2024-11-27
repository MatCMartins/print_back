import jwt
import os
import requests

def handler(event, context):
    # Obter o token do cabeçalho Authorization
    token = event["headers"].get("Authorization", "").replace("Bearer ", "")

    if not token:
        return {"statusCode": 401, "body": "Unauthorized: No token provided"}

    try:
        # Obter chaves públicas do Azure AD
        tenant_id = os.environ["AZURE_AD_TENANT_ID"]
        jwks_url = f"https://login.microsoftonline.com/{tenant_id}/discovery/v2.0/keys"
        jwks = requests.get(jwks_url).json()

        # Decodificar e validar o token
        client_id = os.environ["AZURE_AD_CLIENT_ID"]
        decoded_token = jwt.decode(
            token,
            jwks,
            algorithms=["RS256"],
            audience=client_id,
            options={"verify_exp": True},
        )

        # Token válido
        return {"principalId": decoded_token["sub"], "policyDocument": allow_policy(event["methodArn"])}
    except Exception as e:
        print(f"Token validation error: {e}")
        return {"statusCode": 401, "body": "Unauthorized: Invalid token"}


def allow_policy(method_arn):
    return {
        "Version": "2012-10-17",
        "Statement": [{"Action": "execute-api:Invoke", "Effect": "Allow", "Resource": method_arn}],
    }
