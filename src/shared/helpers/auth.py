import os
from msal import ConfidentialClientApplication
from jwt import decode, DecodeError, ExpiredSignatureError
from jwt.algorithms import RSAAlgorithm

def authenticate(event):
    client_id = os.environ.get("CLIENT_ID")
    client_secret = os.environ.get("CLIENT_SECRET")
    authority = os.environ.get("AUTHORITY")
    scope = ["User.Read"]

    # Instancia o cliente MSAL
    app = ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret,
    )

    # Obtém o token do cabeçalho de autorização
    token = None
    if "Authorization" in event["headers"]:
        auth_header = event["headers"]["Authorization"]
        if auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

    if not token:
        return {"error": "Token de autorização ausente"}, 401

    try:
        jwks_uri = f"{authority}/discovery/v2.0/keys"
        jwks = app.http_client.get(jwks_uri).json()
        key = RSAAlgorithm.from_jwk(jwks["keys"][0])

        # Decodifica e valida o token
        decoded_token = decode(
            token,
            key=key,
            algorithms=["RS256"],
            audience=client_id,
            issuer=f"{authority}/v2.0"
        )

        # Verifica os escopos
        if "scp" not in decoded_token or "User.Read" not in decoded_token["scp"]:
            return {"error": "Escopo inválido"}, 403

        return {"user": decoded_token}, 200

    except ExpiredSignatureError:
        return {"error": "Token expirado"}, 401
    except DecodeError:
        return {"error": "Token inválido"}, 401
    except Exception as e:
        return {"error": f"Erro ao validar token: {str(e)}"}, 500
