from tkinter import *

class InputLengthTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Digit Limit Test")

        self.frame = Frame(root, padx=10, pady=10)
        self.frame.grid()

        self.label = Label(self.frame, text="Enter an amount (max 20 digits):", font=("Arial", 12))
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.input_box = Entry(self.frame, font=("Arial", 14), width=30)
        self.input_box.grid(row=1, column=0, padx=5, pady=5)

        self.result_label = Label(self.frame, text="", font=("Arial", 12), fg="#084C99")
        self.result_label.grid(row=2, column=0, pady=5)

        self.convert_button = Button(self.frame, text="Convert", font=("Arial", 12, "bold"),
                                     bg="#3366CC", fg="white", width=15, command=self.check_input)
        self.convert_button.grid(row=3, column=0, pady=10)

    def check_input(self):
        value = self.input_box.get().strip()

        # Count only digits
        digits_only = ''.join(filter(str.isdigit, value))
        if len(digits_only) > 20:
            self.result_label.config(text="Too many digits, the limit is 20.", fg="#9C0000")
            self.input_box.config(bg="#F4CCCC")
            self.input_box.delete(0, END)
        else:
            self.result_label.config(text="Under 20 digits.", fg="#084C99")
            self.input_box.config(bg="white")


# Run the test GUI
if __name__ == "__main__":
    root = Tk()
    InputLengthTest(root)
    root.mainloop()
