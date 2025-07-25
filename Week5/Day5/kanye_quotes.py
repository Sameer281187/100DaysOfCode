from tkinter import *
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()

    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])


window = Tk()
window.title("Kanye Quotes")
window.config(padx=50, pady=50)

bg_image = PhotoImage(file="background.png")
canvas = Canvas(width=300, height=414)
canvas.create_image(150, 207, image=bg_image)
quote_text = canvas.create_text(150, 207, text="abcd", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=1, column=1)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=2, column=1)





window.mainloop()