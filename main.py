#Password generator

# module
import random
import string

# Function: PassGen
def PassGen():
    alphabet_upper = string.ascii_uppercase # upper case
    alphabet_lower = string.ascii_lowercase# lower case
    numbers = string.digits # numbers
    chars = alphabet_upper + alphabet_lower + numbers # concat together
    chars_len = int(input("Please enter your password length: ")) # input password length
    password = ''
    for i in range(chars_len):
        password += random.choice(chars) # random characther
    print(password)

# Run function
PassGen()
