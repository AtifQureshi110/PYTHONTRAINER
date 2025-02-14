import random
import string

def generate_password(length=8):
    """Generates a random password of the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Real-world example:
print("Generated Password:", generate_password(12))
