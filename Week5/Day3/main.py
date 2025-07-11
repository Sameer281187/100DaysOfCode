from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    language_data = pd.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    language_data = pd.read_csv("data/french_words.csv").to_dict(orient="records")
finally:
    random_word = {}
#----------------------------------METHODS----------------------------------
def get_random_word():
    global flip_timer, random_word
    window.after_cancel(flip_timer)
    random_word = random.choice(language_data)
    canvas.itemconfig(canvas_image, image=card_image_front)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word["French"], fill="black")
    english_translation = random_word["English"]
    flip_timer = window.after(3000, flip_card, english_translation)


def flip_card(eng_word):
    canvas.itemconfig(canvas_image, image= card_image_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=eng_word, fill="white")
    #window.after_cancel(None)

def remove_learnt_word():
    language_data.remove(random_word)
    data = pd.DataFrame(language_data)
    data.to_csv("data/words_to_learn.csv", index=False)
    get_random_word()



#----------------------------------UI SETUP----------------------------------
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, pady= 20, padx=20)

flip_timer = window.after(3000, func=flip_card)

card_image_front = PhotoImage(file="images/card_front.png")
tick_image = PhotoImage(file="images/right.png")
cross_image = PhotoImage(file="images/wrong.png")
card_image_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_image_front)
title_text = canvas.create_text(400, 165, text="", font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 300, text= "", font=('Ariel', 60, 'bold'))
canvas.grid(row=1, column=1, columnspan=2)

tick_button = Button(image=tick_image, highlightthickness=0, command=remove_learnt_word)
tick_button.grid(row=2, column=2)

cross_button = Button(image=cross_image, highlightthickness=0, command=get_random_word)
cross_button.grid(row=2, column=1)

get_random_word()



window.mainloop()



