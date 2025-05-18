from tkinter import *

def check_input():
    value = entry.get()
    try:
        value = float(value)
        if value >= 1:
            currency_message.config(text="Correct")
        else:
            currency_message.config(text="Enter a number more than / equal to 1", fg="red")
    except ValueError:
        currency_message.config(text="Enter a number more than / equal to 1", fg="red")

# GUI setup
root = Tk()
root.title("Input box for currencies")

# Entry box
entry = Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=10)

# Convert button
currency_box = Button(root, text="Convert", font=("Arial", 12, "bold"),
                     bg="#004C99", fg="white", command=check_input)
currency_box.pack(pady=5)

# Message label
currency_message = Label(root, text="", font=("Arial", 12))
currency_message.pack(pady=5)

root.mainloop()
