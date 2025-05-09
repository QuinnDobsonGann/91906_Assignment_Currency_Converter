from tkinter import *


# Dropdown Menu to select currencies
class DropdownComponent:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Dropdown Menu")

        # Main frame
        self.frame = Frame(root, padx=10, pady=10)  # Set background color to orange
        self.frame.grid()

        # Label
        self.label = Label(self.frame, text="Select a currency:", font=("Arial", 12))
        self.label.grid(row=0, column=0, padx=5, pady=5)

        # Dropdown menu
        self.selected_option = StringVar()
        self.selected_option.set("NZD")  # Default selection
        self.dropdown_menu = OptionMenu(self.frame, self.selected_option,
                                        "NZD", "USD", "CAD")
        self.dropdown_menu.config(bg="#FFA500", font=("Arial", 12), highlightbackground="#FFA500")
        self.dropdown_menu.grid(row=0, column=1, padx=5, pady=5)


# Run the GUI
if __name__ == "__main__":
    root = Tk()
    # root.configure()  # Set background color of root window
    DropdownComponent(root)
    root.mainloop()
