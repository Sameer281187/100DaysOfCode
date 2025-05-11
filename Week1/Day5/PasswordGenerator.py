import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "?"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

no_of_letters = int(input("Enter the number of letters that you want in your password: "))
no_of_symbols = int(input("Enter the number of symbols that you want in your password: "))
no_of_numbers = int(input("Enter the number of numbers that you want in your password: "))

password_char_list = []
for i in range(0, no_of_letters):
    password_char_list.append(random.choice(letters))

for i in range(0, no_of_symbols):
    password_char_list.append(random.choice(symbols))

for i in range(0, no_of_numbers):
    password_char_list.append(random.choice(numbers))

random.shuffle(password_char_list)

final_password =""
for char in password_char_list:
    final_password += char

print(final_password)
