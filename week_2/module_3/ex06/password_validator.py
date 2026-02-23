import string

def is_valid_password(password: str) -> bool:
    """Verify if the password has correct length and certain types of characters."""
    if len(password) < 8:
        print("Minimum 8 characteres")
        return False
    if len(password) > 16:
        print("Maximum 16 characteres")
        return False
    if not any(c.isupper() for c in password):
        print("Should contain at least 1 uppercase letter")
        return False
    if not any(c.islower() for c in password):
        print("Should contain at least 1 lowercase letter")
        return False
    if not any(c.isdigit() for c in password):
        print("Should contain at least 1 digit")
        return False
    if not any(c in string.punctuation for c in password):
        print("Should contain at least 1 special character")
        return False
    if any(c in string.whitespace for c in password):
        print("Cannot contain whitespace")
        return False
    return True
