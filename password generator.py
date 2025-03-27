import random
import string
import secrets

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """Generates a strong password with customizable character sets."""
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")
    
    char_sets = []
    if use_upper:
        char_sets.append(string.ascii_uppercase)
    if use_lower:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_special:
        char_sets.append(string.punctuation)
    
    if not char_sets:
        raise ValueError("At least one character set must be selected.")
    
    all_chars = ''.join(char_sets)
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    
    return password

def generate_passphrase(words=4):
    """Generates a passphrase using common words for easier memorability."""
    word_list = ["battery", "horse", "staple", "correct", "monkey", "laptop", "guitar", "ocean", "forest", "sunset"]
    return '-'.join(secrets.choice(word_list) for _ in range(words))

def evaluate_strength(password):
    """Evaluates password strength based on length and character diversity."""
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    return strength_levels[score]

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
    print("Strength:", evaluate_strength(password))
    
    print("\nGenerated Passphrase:", generate_passphrase())
