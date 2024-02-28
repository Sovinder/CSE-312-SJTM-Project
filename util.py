from password_strength import PasswordPolicy
import secrets

def validate_password(password:str):
    policy = PasswordPolicy.from_names(
        length=8,
        uppercase=1,
        numbers=1,
        special=1,
        nonletters=0,
    )
    return policy.test(password)

def generate_auth_token(length:int):
    token = secrets.token_hex(length)
    return token