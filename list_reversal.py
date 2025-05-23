all_calculations = ['10NZD is 5.97USD', '20NZD is 11.94USD',
                    '30NZD is 13.51GBP', '40NZD is 32.94CAD',
                    '50NZD is 29.86USD', '60NZD is 27.02GBP']

newest_first = list(reversed(all_calculations))

print("==== Oldest to Newest for File ====")
for item in all_calculations:
    print(item)

print()

print("==== Most Recent First ===")
for item in newest_first:
    print(item)
