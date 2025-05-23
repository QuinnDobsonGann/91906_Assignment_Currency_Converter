from tkinter import *


class InputLengthTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Digit Limit Test")

        self.frame = Frame(root, padx=10, pady=10)
        self.frame.grid()

        self.label = Label(self.frame, text="Enter an amount (max 7 digits):", font=("Arial", 12))
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.input_box = Entry(self.frame, font=("Arial", 14), width=30)
        self.input_box.grid(row=1, column=0, padx=5, pady=5)
        self.input_box.bind("<Return>", self.check_input)  # Trigger check on Enter key

        self.result_label = Label(self.frame, text="", font=("Arial", 12), fg="#084C99")
        self.result_label.grid(row=2, column=0, pady=5)

    def check_input(self, event=None):
        value = self.input_box.get().strip()
        digits_only = ''.join(filter(str.isdigit, value))

        if len(digits_only) > 7:
            self.result_label.config(text="Too many digits, the limit is 7.", fg="#9C0000")
            self.input_box.config(bg="#F4CCCC")
        else:
            self.result_label.config(text="Under 7 digits", fg="#084C99")
            self.input_box.config(bg="white")


# Runs the application
if __name__ == "__main__":
    root = Tk()
    InputLengthTest(root)
    root.mainloop()
