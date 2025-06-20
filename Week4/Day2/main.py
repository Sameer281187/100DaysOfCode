INVITED_LIST_OF_NAMES = "Input/Names/invited_names.txt"
INVITATION_LETTER_TEMPLATE = "Input/Letters/starting_letter.txt"
OUTPUT_DESTINATION = "Output/ReadyToSend/"
PLACEHOLDER = "[name]"

def get_names(filename):
    with open(filename) as guests:
        invited_names = guests.readlines()
    return invited_names

def read_sample_letter(filename):
    with open(filename, "r") as sample:
        sample_letter = sample.read()
    return sample_letter

def create_invitation_letter_at_destination(filename, content):
    with open(filename, "w") as invitation:
        invitation.write(content)

guest_list = get_names(INVITED_LIST_OF_NAMES)
letter_template = read_sample_letter(INVITATION_LETTER_TEMPLATE)

for name in guest_list:
    final_letter = letter_template.replace(PLACEHOLDER, name.strip("\n"))
    create_invitation_letter_at_destination(f"{OUTPUT_DESTINATION}letter_for_{name.strip("\n")}.txt", final_letter)