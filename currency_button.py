from tkinter import *

def currency_action():
    print("Test click")

root = Tk()
root.title("Currency Button")

# Currency button
currency_button = Button(
    root,
    text="Currency",
    bg="#990099",
    fg="#FFFFFF",
    font=("Arial", 12, "bold"),
    width=12,
    command=currency_action
)
currency_button.grid(padx=5, pady=5)

root.mainloop()
