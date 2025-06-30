from tkinter import *

window = Tk()
window.title("Test Window")
window.minsize(width=500, height= 400)
window.config(padx=20, pady= 20)

my_label = Label(text= "New Label", font= ("Ariel", 12))
my_label.grid(column=0, row=0)

button1 = Button(text= "Button1")
button1.grid(column=1, row= 1)

button2 = Button(text= "Button2")
button2.grid(column=2, row=0)

entry = Entry()
entry.grid(column=3, row=3)

window.mainloop()