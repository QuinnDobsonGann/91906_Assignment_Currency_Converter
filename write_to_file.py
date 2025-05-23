from datetime import date

calculations = ['10NZD is 5.97USD', '20NZD is 11.94USD',
                '30NZD is 13.51GBP', '40NZD is 32.94CAD',
                '50NZD is 29.86USD', '60NZD is 27.02GBP']

# **** Get current date for heading and file name ****
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

file_name = f"currencies_{year}_{month}_{day}"
write_to = f"{file_name}.txt"

with open(write_to, "w") as text_file:

    text_file.write("***** Currency Calculations ******\n")
    text_file.write(f"Generated: {day}/{month}/{year}\n\n")
    text_file.write("Here is your calculation history (oldest to newest)...\n")

    # write the item to file
    for item in calculations:
        text_file.write(item)
        text_file.write("\n")



