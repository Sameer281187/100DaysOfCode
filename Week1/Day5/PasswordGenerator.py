import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "?"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

no_of_letters = random.randint(8,10)
no_of_symbols = random.randint(2,4)
no_of_numbers = random.randint(2,4)

letters_list = [random.choice(letters) for _ in range(no_of_letters)]
    # for i in range(0, no_of_letters):
    #     password_char_list.append(random.choice(letters))
symbol_list = [random.choice(symbols) for _ in range(no_of_symbols)]
    # for i in range(0, no_of_symbols):
    #     password_char_list.append(random.choice(symbols))
number_list = [random.choice(numbers) for _ in range(no_of_numbers)]
    # for i in range(0, no_of_numbers):
    #     password_char_list.append(random.choice(numbers))
password_char_list = letters_list + symbol_list + number_list
random.shuffle(password_char_list)

final_password = "".join(password_char_list)
# for char in password_char_list:
#     final_password += char

print(final_password)
