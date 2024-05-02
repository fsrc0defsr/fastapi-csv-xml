import secrets

def generate_token():
    token = secrets.token_urlsafe(16)
    return token

new_token = generate_token()
print(new_token)