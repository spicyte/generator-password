import random
import string

def generator_password(min_lenght, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    print(letters, digits, special)

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special


    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True


        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

        return pwd   

min_lenght = int(input("Enter the min len: "))
has_number = input("Do you want to habe numbers (y/n)? ").lower() == "y"
has_special = input("Dou u want to have special characters (y/n)?").lower() == "y"
pwd = generator_password(min_lenght, has_number, has_special)
print("Password:", pwd)
 