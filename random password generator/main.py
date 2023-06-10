
import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_special_chars=False):
     # Character set to use
     charset = ''

     if use_letters:
         charset += string.ascii_letters

     if use_numbers:
         charset += string.digits

     if use_special_chars:
         charset += "!#$%&@€₺" # Special characters are defined here, can be changed as desired.

     # Creating the password
     password = ''.join(random.choice(charset) for _ in range(length))
     return password

# Receiving input from user
length = int(input("Enter password length: "))
use_letters = input("Do you want to use letters? (Yes: 'e', No: 'h'): ").lower() == 'e'
use_numbers = input("Do you want to use numbers? (Yes: 'e', No: 'h'): ").lower() == 'e'
use_special_chars = input("Do you want to use special characters? (Yes: 'e', No: 'h'): ").lower() == 'e'

# Creating the password
password = generate_password(length, use_letters, use_numbers, use_special_chars)
print("Password generated:", password)

