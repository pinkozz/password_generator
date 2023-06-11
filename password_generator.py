import secrets
import string

ask = input('How long do you want your password to be?: ')

letters_digits = string.ascii_letters + string.digits
password = ''

for i in range(int(ask)):
    digit = secrets.choice(letters_digits)
    password += digit

print(password)