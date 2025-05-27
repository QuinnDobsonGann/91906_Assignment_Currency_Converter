from tkinter import *
from functools import partial  # to prevent unwanted windows
import conversion_roundingv2 as cr
from datetime import date


# main GUI
class Converter:
    """
    Currency conversion tool (NZD to either USD, CAD and GBP)
    """

    def __init__(self):
        """
        Currency converter GUI
        """

        self.all_calculations_list = []

        self.currency_frame = Frame(padx=10, pady=10)
        self.currency_frame.grid()

        self.currency_heading = Label(self.currency_frame,
                                      text="Currency Convertor",
                                      font=("Arial", "16", "bold")
                                      )
        self.currency_heading.grid(row=0)

        instructions = (
            "Please enter a Currency below and then press "
            "one of the buttons to convert it from NZD "
            "to either USD, CAD and GBP. Can only convert above the number of 1, maximum input of digits is 7. "
            "Converts your calculation to two decimal places. \n\n"
            "NZD is New Zealand Dollar,"
            "USD is United States Dollar, CAD is Canadian Dollar and "
            "GBP is Great British Pound."
        )

        self.currency_instructions = Label(self.currency_frame,
                                           text=instructions,
                                           wraplength=250, width=40,
                                           justify="left")
        self.currency_instructions.grid(row=1)

        self.currency_entry = Entry(self.currency_frame,
                                    font=("Arial", "14")
                                    )
        self.currency_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.answer_error = Label(self.currency_frame, text=error,
                                  fg="#084C99", font=("Arial", "14", "bold"))
        self.answer_error.grid(row=3)

        # Frame for top conversion buttons
        self.top_button_frame = Frame(self.currency_frame)
        self.top_button_frame.grid(row=4, column=0)

        # Frame for bottom buttons (Help / Info and History / Export)
        self.bottom_button_frame = Frame(self.currency_frame)
        self.bottom_button_frame.grid(row=5, column=0, pady=(10, 0))

        # button list (button text | bg colour | command | frame | row | column)
        button_details_list = [
            # Top buttons
            ["To USD", "#990099", partial(self.check_currency, "USD"), self.top_button_frame, 0, 0],
            ["To CAD", "#009900", partial(self.check_currency, "CAD"), self.top_button_frame, 0, 1],
            ["To GBP", "#909900", partial(self.check_currency, "GBP"), self.top_button_frame, 0, 2],

            # Bottom buttons
            ["Help / Info", "#CC6600", self.to_help, self.bottom_button_frame, 0, 0],
            ["History / Export", "#004C99", self.to_history, self.bottom_button_frame, 0, 1],
        ]

        # list to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(item[3],
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[4], column=item[5], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[4]
        self.to_history_button.config(state=DISABLED)

        # keep help button ref for enabling later
        self.to_help_button = self.button_ref_list[3]

    # checks the correct inputs
    def check_currency(self, currency_target):
        to_convert = self.currency_entry.get()
        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.currency_entry.config(bg="#FFFFFF")

        error = f"Enter a number more than / equal to 1"
        has_errors = "no"

        digits_only = ''.join(filter(str.isdigit, to_convert))
        if len(digits_only) > 7:
            has_errors = "yes"
            error = "Too many digits (limit of digits is 7)."
        else:
            try:
                to_convert = float(to_convert)
                if to_convert >= 1:
                    self.convert(currency_target, to_convert)
                else:
                    has_errors = "yes"
            except ValueError:
                has_errors = "yes"

        if has_errors == "yes":
            self.answer_error.config(text=error, fg="#9C0000", font=("Arial", "10", "bold"))
            self.currency_entry.config(bg="#F4CCCC")
            self.currency_entry.delete(0, END)

    # shows the conversion between currencies(NZD to either USD,CAD,GBP).
    def convert(self, currency_target, to_convert):
        if currency_target == "USD":
            answer = cr.to_usd(to_convert)
        elif currency_target == "CAD":
            answer = cr.to_cad(to_convert)
        elif currency_target == "GBP":
            answer = cr.to_gbp(to_convert)
        else:
            answer = "Error"

        answer_statement = f"{to_convert}NZD is {answer}{currency_target}"
        self.to_history_button.config(state=NORMAL)
        self.to_help_button.config(state=NORMAL)
        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer_statement)

    def to_help(self):
        DisplayHelp(self)

    def to_history(self):
        HistoryExport(self, self.all_calculations_list)


# shows help GUI when clicked
class DisplayHelp:

    def __init__(self, partner):
        background = "#ffe6cc"
        self.help_box = Toplevel()
        partner.to_help_button.config(state=DISABLED)

        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        # help / info text
        help_text = "To use the program, simply enter the currency " \
                    "you wish to convert, starting at the default currency NZD, and then choose to convert " \
                    "to either USD,CAD, GBP.\n\nNZD is New Zealand Dollar, USD is United States Dollar and CAD is " \
                    "Canadian Dollar. Can only convert above the number of 1, maximum input of digits is 7. Rounds " \
                    "answer to two decimal places. \n\n" \
                    "To see your calculation history and export it to a text file, please click the 'History / " \
                    "Export' button.\n\n You can open multiple History / Export windows when you have done the 5 max" \
                    "calculations per window. You can then export multiple windows with your 5 calculations."

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    # closes help menu and destroys it completely.
    def close_help(self, partner):
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


class HistoryExport:

    # used to create file and store the currencies on a file
    def __init__(self, partner, calculations):
        self.history_box = Toplevel()
        partner.to_history_button.config(state=DISABLED)

        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        if len(calculations) <= 5:
            calc_back = "#D5E8D4"
            calc_amount = "all your"
        else:
            calc_back = "#ffe6cc"
            calc_amount = (f"your recent calculations - "
                           f"showing {5} / {len(calculations)}")

        recent_intro_txt = (f"Below are {calc_amount} calculations "
                            "(to the nearest currency). Maximum of 5 calculations appear.")

        newest_first_string = ""
        newest_first_list = list(reversed(calculations))

        # calculations(max is 5 for export)
        if len(newest_first_list) <= 5:
            for item in newest_first_list[:-1]:
                newest_first_string += item + "\n"
            newest_first_string += newest_first_list[-1]
        else:
            for item in newest_first_list[:5 - 1]:
                newest_first_string += item + "\n"
            newest_first_string += newest_first_list[5 - 1]

        export_instruction_txt = ("Please push <Export> to save your calculations in "
                                  "file. If the filename already exists, it will be replaced.")

        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt, ("Arial", "11",), None],
            [newest_first_string, ("Arial", "14"), calc_back],
            [export_instruction_txt, ("Arial", "11"), None],
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0], font=item[1],
                               bg=item[2], wraplength=300, justify="left", pady=10, padx=20)
            make_label.grid(row=count)
            history_label_ref.append(make_label)

        self.export_filename_label = history_label_ref[3]

        self.history_button_frame = Frame(self.history_box)
        self.history_button_frame.grid(row=4)

        # export button, use to close
        button_details_list = [
            ["Export", "#004C99", lambda: self.export_data(calculations), 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]

        for btn in button_details_list:
            self.make_button = Button(self.history_button_frame,
                                      font=("Arial", "12", "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#FFFFFF", width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

    # records when the export data was taken
    def export_data(self, calculations):
        today = date.today()
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        file_name = f"Currencies_{year}_{month}_{day}"
        success_string = f"Export Successful! The file is called {file_name}.txt"
        self.export_filename_label.config(bg="#009900", text=success_string,
                                          font=("Arial", "12", "bold"))

        with open(f"{file_name}.txt", "w") as text_file:
            text_file.write("***** Currency Calculations ******\n")
            text_file.write(f"Generated: {day}/{month}/{year}\n\n")
            text_file.write("Here is your calculation history (oldest to newest)...\n")
            for item in calculations:
                text_file.write(item + "\n")

    #  closes the window and destroys it
    def close_history(self, partner):
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Currency Convertor")
    Converter()
    root.mainloop()
