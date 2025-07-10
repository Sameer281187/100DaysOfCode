from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
               "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    symbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "?"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_char_list = letters_list + symbol_list + number_list
    random.shuffle(password_char_list)

    final_password = "".join(password_char_list)
    password_entry.insert(0,final_password)

    window.clipboard_clear()
    window.clipboard_append(final_password)
    window.update()

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data_to_file():
    new_data = {
        website_entry.get(): {
            "username" : username_entry.get(),
            "password" : password_entry.get()
        }
    }
    if len(website_entry.get()) == 0:
        messagebox.showinfo(title="Missing Details", message="The Website field cannot be left empty.")
    elif len(username_entry.get()) == 0:
        messagebox.showinfo(title="Missing Details", message="The username field cannot be left empty.")
    elif len(password_entry.get()) == 0:
        messagebox.showinfo(title="Missing Details", message="The password field cannot be left empty.")
    else:
        user_response = messagebox.askokcancel(title=f"Verify credentials for {website_entry.get()}",
                                               message=f"The entered details for {website_entry.get()} are as follows: \n"
                                                       f"Username: {username_entry.get()} \n"
                                                       f"Password: {password_entry.get()} \n"
                                                       f"Confirm if the details are correct ?")
        if user_response:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            messagebox.showinfo(title="Data Saved Successfully", message="Your data is saved successfully")

# ---------------------------- SEARCH EXISTING PASSWORDS ------------------------------- #
def find_password():
    website = website_entry.get().title()
    is_value_present = False
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title="No Data File Found", message="You do not have details saved for any of your account")
    else:
        for key in data.keys():
            if key == website:
                is_value_present = True
                break
        if is_value_present:
            messagebox.showinfo(title="Your Details", message=f"Here are your credentials for {key}: \n"
                                                              f"Username: {data[key]["username"]}\n"
                                                              f"Password: {data[key]["password"]}")
        else:
            messagebox.showinfo(title="No Details Exist", message="You do not have any saved details for this account")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=2)

website_label = Label(text="Website:")
website_label.grid(row=2, column=1)
website_label.config(padx=5, pady= 5)

username_label = Label(text="Email/Username:")
username_label.grid(row=3, column=1)
username_label.config(padx=5, pady= 5)

password_label = Label(text="Password:")
password_label.grid(row=4, column=1)
password_label.config(padx=5, pady= 5)

website_entry = Entry(width=34)
website_entry.grid(row=2, column=2)
website_entry.focus()

username_entry = Entry(width=55)
username_entry.grid(row=3, column=2, columnspan=2)
username_entry.insert(0, "abc@xyz.com")

password_entry = Entry(width=34)
password_entry.grid(row=4, column=2)

add_button = Button(text="Add", width=47, command=save_data_to_file)
add_button.grid(row=5, column=2, columnspan=2)

generate_password_button = Button(text="Generate Password", width=16, command=generate_password)
generate_password_button.grid(row=4, column=3)

search_button = Button(text="Search", width=16, command=find_password)
search_button.grid(row=2, column=3)

window.mainloop()