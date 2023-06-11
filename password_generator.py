import secrets
import string

#Ask about the length of the password
ask = input('How long do you want your password to be?: ')

#Create a variable that contains all numbers and letters
letters_digits = string.ascii_letters + string.digits

password = ''

for i in range(int(ask)):                           #Repeat the process a certain amount of times
    character = secrets.choice(letters_digits)      #Generate one character
    password += digit                               #Add the digit to the password

print(password)
