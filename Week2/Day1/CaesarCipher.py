
def message_encoding(code_type, message, shift_no, alphabets):
    result = ""
    if code_type.lower() == "encode":
        encrypted_message = ""
        for char in message:
            index = 0
            if char.lower() == " ":
                encrypted_message += char
            for i in range(len(alphabets)):
                if char.lower() == alphabets[i]:
                    index = (i + shift_no) % len(alphabets)
                    encrypted_message += alphabets[index]
        result = encrypted_message

    if code_type.lower() == "decode":
        decrypted_message = ""
        for char in message:
            if char.lower() == " ":
                decrypted_message += char
            for i in range(len(alphabets)):
                if char.lower() == alphabets[i]:
                    index = i - shift_no
                    decrypted_message += alphabets[index]
        result = decrypted_message

    return result

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run_prog = True

print()

while run_prog:
    code_type = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    print(code_type)

    message = input("Please type your message: ")
    print(message)

    shift_no = int(input("Type the shift no. : "))
    print(shift_no)

    final_message = message_encoding(code_type, message, shift_no, alphabets)

    if code_type == 'encode':
        print("Here's the encoded result:", final_message)
    else:
        print("Here's the decoded result:", final_message)

    want_to_continue = input("Type 'yes' if you want to go again, otherwise Type 'no'.")

    if want_to_continue.lower() == 'no':
        run_prog = False