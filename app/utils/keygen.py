import secrets
import string


def generate_random_key(length: int = 8) -> str:
    """Generate a random key"""
    characters = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))
