import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the desired length for each password: "))
        
        if num_passwords <= 0 or password_length <= 0:
            print("Please enter valid positive integers.")
            return

        for _ in range(num_passwords):
            password = generate_password(password_length)
            print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
