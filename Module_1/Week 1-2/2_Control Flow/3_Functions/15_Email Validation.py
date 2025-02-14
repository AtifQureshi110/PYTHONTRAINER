def is_valid_email(email):
    """Checks if the email contains '@' and '.' to determine validity."""
    if "@" in email and "." in email:
        return True
    else:
        return False

# Real-world example:
email = "user@example.com"
if is_valid_email(email):
    print("Valid Email!")
else:
    print("Invalid Email!")
