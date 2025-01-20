import random
import string

def generate_password(length):
    # Use letters and digits for the password
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Welcome to the Simple Password Generator!")
    
    # Get desired length of the password from the user
    length = int(input("Enter the desired length of the password (minimum 5): "))
    
    if length < 5:
        print("Please enter a length of at least 5.")
        return

    # Generate and display the password
    print(f"Generated Password: {generate_password(length)}")

# Run the password generator
if __name__ == "__main__":
    main()
