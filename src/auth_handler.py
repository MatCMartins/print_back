import os
import jwt
import requests
from aws_lambda_powertools.utilities.parser import event_parser  # Opcional, para melhorar a estrutura do evento

AZURE_AD_CLIENT_ID = os.environ["AZURE_AD_CLIENT_ID"]
AZURE_AD_TENANT_ID = os.environ["AZURE_AD_TENANT_ID"]

def auth_handler(event, context):
    # Recupera o token do cabeçalho de autorização
    token = event["headers"].get("Authorization", "").replace("Bearer ", "")
    if not token:
        return {"statusCode": 401, "body": "Unauthorized"}

    # Validação do token JWT
    try:
        # URL para recuperar as chaves públicas do Azure AD
        public_keys_url = f"https://login.microsoftonline.com/{AZURE_AD_TENANT_ID}/discovery/v2.0/keys"
        public_keys = requests.get(public_keys_url).json()["keys"]

        # Decodifica o token JWT
        decoded = jwt.decode(
            token,
            key=public_keys[0],
            algorithms=["RS256"],
            audience=AZURE_AD_CLIENT_ID,  # Confirma que o token foi emitido para o cliente correto
        )
    except jwt.ExpiredSignatureError:
        return {"statusCode": 401, "body": "Token expired"}
    except jwt.InvalidTokenError:
        return {"statusCode": 401, "body": "Invalid token"}

    # Token válido; retorna as informações do usuário
    user_email = decoded.get("email", "unknown_user")
    return {"statusCode": 200, "body": f"Welcome {user_email}"}
