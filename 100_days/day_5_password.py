import random

letters = ['a', 'b', 'c','d','e','f','g','h']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*']

nr_letters = input('How many letters do you want in your password?')
nr_numbers = input('How many numbers do you want in your password?')
nr_symbols = input('How many symbols do you want in your password?')

password = []

for x in range(0, int(nr_letters)):
    index = random.randint(0, len(letters)-1)
    password.append(letters[index])

for x in range(0, int(nr_numbers)):
    index = random.randint(0, len(numbers)-1)
    password.append(numbers[index])

for x in range(0, int(nr_symbols)):
    index = random.randint(0, len(symbols)-1)
    password.append(symbols[index])

print(password)

password_aux = []

while len(password) > 0:
    char = password[random.randint(0, len(password)-1)]
    password_aux.append(char)
    password.remove(char)

print(password_aux)