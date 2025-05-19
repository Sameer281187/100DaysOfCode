def modify_message(message, shift_no, encoding):
    resultant_message = ""
    shift_no = shift_no * (-1) if encoding == 'decode' else shift_no
    for char in message:
        index = 0
        if char.lower() == " ":
            resultant_message += char
        else:
            for letter in alphabets:
                if char.lower() == letter:
                    resultant_message += alphabets[(alphabets.index(letter) + shift_no) % 26]
    print(f"Here's the {encoding}d result: {resultant_message}")


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run_prog = True

while run_prog:
    code_type = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    print(code_type)

    message = input("Please type your message: ")
    print(message)

    shift_no = int(input("Type the shift no. : "))
    print(shift_no)

    modify_message(message, shift_no, code_type)

    want_to_continue = input("Type 'yes' if you want to go again, otherwise Type 'no'.")

    run_prog = False if want_to_continue.lower() == "no" else True
