import os
from msal import ConfidentialClientApplication

def authenticate(event):
    client_id = os.environ.get("CLIENT_ID")
    client_secret = os.environ.get("CLIENT_SECRET")
    authority = os.environ.get("AUTHORITY")
    scope = ["User.Read"]

    app = ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret,
    )

    token = None
    if "Authorization" in event["headers"]:
        auth_header = event["headers"]["Authorization"]
        token = auth_header.split(" ")[1]

    if token:
        result = app.acquire_token_silent(scope, account=None)
        if not result:
            result = app.acquire_token_for_client(scopes=scope)
        
        if "access_token" in result:
            return result["access_token"]
    
    return None