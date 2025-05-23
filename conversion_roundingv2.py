def round_ans(val):
    """
    Rounds currency to the nearest whole number.
    :param val: Number to be rounded
    :return: Number rounded to the nearest whole number
    """
    var_rounded = round(val, 2)
    return "{:.2f}".format(var_rounded)


def to_nzd(to_convert):
    """
    Starting currency(default)
    """
    answer = to_convert * 1.2  # Example conversion rate from CAD to NZD
    return round_ans(answer)


def to_cad(to_convert):
    """
    Converts from NZD to CAD.
    """
    answer = to_convert * 0.82340  # Example conversion rate from NZD to CAD
    return round_ans(answer)


def to_usd(to_convert):
    """
    Converts from NZD to USD.
    """
    answer = to_convert * 0.59720  # Example conversion rate from NZD to USD
    return round_ans(answer)


def to_gbp(to_convert):
    """
     Converts from NZD to GBP.
     """
    answer = to_convert * 0.4503  # Example conversion rate from NZD to USD
    return round_ans(answer)

    # Main routine / Testing starts here

# to_test = [10, 50, 100]

# for item in to_test:
#    print(f"{item} CAD is {to_nzd(item)} NZD")
#    print(f"{item} NZD is {to_cad(item)} CAD")
#    print(f"{item} NZD is {to_usd(item)} USD")
#    print(f"[item] NZD is {to_gbp(item)} GBP")
#    print()
