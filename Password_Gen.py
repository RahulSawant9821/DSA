''' Create lists containing lowercase letters, uppercase letters, digits, and special characters.
Use random module functions (random.choice()) to generate a random password of a specified length, ensuring it includes characters from all categories.'''
import random
def Generate_Password(length):
    password = " "
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = lowercase_letters.upper()
    digits = "0123456789"
    special_characters = "!@#$%^&*()"

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    password= (
        random.choice(lowercase_letters)+
        random.choice(uppercase_letters)+
        random.choice(digits)+
        random.choice(special_characters)
    )

    password += "".join(random.choice(all_characters) for _ in range(length-4))

    return password






Password_length = int(input("Enter the optimal length of the password :"))

your_password = Generate_Password(Password_length)

print(f"Your password is : {your_password}")

