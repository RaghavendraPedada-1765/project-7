import string
import random
import sys

try:
    import pyperclip
    HAS_CLIPBOARD = True
except ImportError:
    HAS_CLIPBOARD = False

def generate_password(length, use_special, use_digits):
    chars = list(string.ascii_letters)
    if use_digits:
        chars += list(string.digits)
    if use_special:
        chars += list(string.punctuation)
    if not chars:
        raise ValueError("No characters to choose from!")
    # Guarantee at least one digit/special if selected
    password = []
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    while len(password) < length:
        password.append(random.choice(chars))
    random.shuffle(password)
    return ''.join(password[:length])

def main():
    print("=== Password Generator Tool ===")
    try:
        length = int(input("Enter password length (min 4): "))
        if length < 4:
            print("Password length must be at least 4.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Length must be a number.")
        sys.exit(1)
    special = input("Include special characters? (y/n): ").lower() == "y"
    digits = input("Include digits? (y/n): ").lower() == "y"
    pwd = generate_password(length, special, digits)
    print("\nGenerated password:", pwd)

    opt = input("Save password to file? (y/n): ").lower()
    if opt == "y":
        fname = input("Enter filename (default: password.txt): ").strip() or "password.txt"
        with open(fname, "a") as f:
            f.write(pwd + "\n")
        print(f"Password saved to {fname}")

    if HAS_CLIPBOARD:
        opt = input("Copy password to clipboard? (y/n): ").lower()
        if opt == "y":
            pyperclip.copy(pwd)
            print("Password copied to clipboard!")
    else:
        print("(Install 'pyperclip' for clipboard support)")

if __name__ == "__main__":
    main()
