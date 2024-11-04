import random
import string

def generate_password(num_letters, num_numbers, num_symbols, specific_letters="", specific_numbers="", specific_symbols=""):
    # Remove any spaces from specific characters
    specific_letters = specific_letters.replace(" ", "")
    specific_numbers = specific_numbers.replace(" ", "")
    specific_symbols = specific_symbols.replace(" ", "")
    
    # Define possible characters
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    # Start with specific characters requested by the user
    password_letters = ''.join(random.choice(letters) for _ in range(num_letters - len(specific_letters))) + specific_letters
    password_numbers = ''.join(random.choice(numbers) for _ in range(num_numbers - len(specific_numbers))) + specific_numbers
    password_symbols = ''.join(random.choice(symbols) for _ in range(num_symbols - len(specific_symbols))) + specific_symbols
    
    # Combine all characters and shuffle
    password_characters = list(password_letters + password_numbers + password_symbols)
    random.shuffle(password_characters)
    password = ''.join(password_characters)
    return password

def password_strength(length, num_letters, num_numbers, num_symbols):
    """Basic strength estimator based on length and character variety"""
    score = length + (num_letters > 0) + (num_numbers > 0) + (num_symbols > 0)
    if score >= 12:
        return "Strong"
    elif score >= 8:
        return "Moderate"
    else:
        return "Weak"

def suggest_password(num_letters, num_numbers, num_symbols, specific_letters="", specific_numbers="", specific_symbols=""):
    # Suggest a password based on the specified criteria
    suggested_password = generate_password(num_letters, num_numbers, num_symbols, specific_letters, specific_numbers, specific_symbols)
    return suggested_password

def main():
    while True:
        # Get the total password length
        total_length = int(input("Enter the desired total password length: "))
        
        # Get user input for the number of letters, numbers, and symbols
        print("Enter the number of each character type you'd like in your password:")
        num_letters = int(input("How many letters? "))
        num_numbers = int(input("How many numbers? "))
        num_symbols = int(input("How many symbols? "))
        
        # Check if the total length matches the sum of the specified characters
        if num_letters + num_numbers + num_symbols != total_length:
            print("Error: The sum of letters, numbers, and symbols must equal the total length.")
            continue

        # Ask user if they want to include any specific characters in each category
        specific_letters = input("Enter specific letters you want to include (or leave blank): ")
        specific_numbers = input("Enter specific numbers you want to include (or leave blank): ")
        specific_symbols = input("Enter specific symbols you want to include (or leave blank): ")

        # Determine password strength based on criteria
        strength = password_strength(total_length, num_letters, num_numbers, num_symbols)
        print(f"Password strength based on criteria: {strength}")

        # Generate and display three passwords based on user preference
        passwords = [generate_password(num_letters, num_numbers, num_symbols, specific_letters, specific_numbers, specific_symbols) for _ in range(3)]
        
        # Suggest a password
        suggested_password = suggest_password(num_letters, num_numbers, num_symbols, specific_letters, specific_numbers, specific_symbols)
        
        print("\nGenerated Password(s):")
        for idx, password in enumerate(passwords, 1):
            print(f"{idx}. {password}")

        print(f"Suggested Password: {suggested_password}")
        
        # Save passwords to a file if the user chooses
        save_choice = input("Would you like to save the passwords to a file? (y/n): ").strip().lower()
        if save_choice == 'y':
            with open("generated_passwords.txt", "w") as file:
                for idx, password in enumerate(passwords, 1):
                    file.write(f"{idx}. {password}\n")
                file.write(f"Suggested Password: {suggested_password}\n")  # Save the suggested password as well
            print("Passwords saved to generated_passwords.txt")
        
        # Ask if the user wants to generate more passwords or exit
        repeat_choice = input("Do you want to generate more passwords? (y/n): ").strip().lower()
        if repeat_choice != 'y':
            print("Exiting Password Generator.")
            break

if __name__ == "__main__":
    main()
