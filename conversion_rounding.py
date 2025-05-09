def round_ans(val):
    """
    Rounds currency to the nearest whole number.
    :param val: Number to be rounded
    :return: Number rounded to the nearest whole number
    """
    var_rounded = round(val, 2)
    return "{:.0f}".format(var_rounded)


def to_nzd(to_convert):
    """
    Converts from CAD or USD to NZD.
    :param to_convert: Amount in CAD or USD
    :return: Converted amount in NZD
    """
    answer = to_convert * 1.18  # Example conversion rate from CAD to NZD
    return round_ans(answer)


def to_cad(to_convert):
    """
    Converts from NZD or USD to CAD.
    :param to_convert: Amount in NZD or USD
    :return: Converted amount in CAD
    """
    answer = to_convert * 0.85  # Example conversion rate from NZD to CAD
    return round_ans(answer)


def to_usd(to_convert):
    """
    Converts from NZD or CAD to USD.
    :param to_convert: Amount in NZD or CAD
    :return: Converted amount in USD
    """
    answer = to_convert * 0.62  # Example conversion rate from NZD to USD
    return round_ans(answer)


# Main routine / Testing starts here
to_test = [10, 50, 100]

for item in to_test:
    print(f"{item} CAD is {to_nzd(item)} NZD")
    print(f"{item} NZD is {to_cad(item)} CAD")
    print(f"{item} NZD is {to_usd(item)} USD")
    print()
