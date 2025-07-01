from tkinter import *

window = Tk()
window.title("Miles to KM")
window.minsize(250, 150)
window.config(padx= 30, pady= 20)

def convert_to_km():
    km_value = float(miles_entry.get()) * 1.60934
    result_value.config(text=f"{(round(km_value, 2))}")

miles_label = Label(text= "Miles", font= ("Ariel", 11))
miles_label.grid(column=4, row=2)
miles_label.config(padx=5, pady=5)

is_equal_to_label = Label(text="is equal to", font= ('Ariel', 11))
is_equal_to_label.grid(column= 2, row= 3)
is_equal_to_label.config(padx=5, pady=5)

km_label = Label(text= "Km", font= ('Ariel', 11))
km_label.grid(column=4, row=3)
km_label.config(padx=5, pady=5)

result_value = Label(text= " ", font= ('Ariel', 11))
result_value.grid(column=3, row=3)
result_value.config(padx=5, pady=5)


miles_entry = Entry(width= 10)
miles_entry.grid(column=3, row=2)

calculate_button = Button(text= "Calculate", command= convert_to_km)
calculate_button.grid(column=3, row=4)
calculate_button.config(padx=5, pady=5)


window.mainloop()