def round_ans(val):
    """
    Rounds temperature to nearest degree
    :param val: Number to be rounded
    :return: Number rounded to nearest degree
    """
    var_rounded = round(val)
    return "{:.0f}".format(var_rounded)


def to_usd(to_convert):
    """
    Converts from °F to °C
    :param to_convert: Temperature to be converted in °F
    :return: Converted temperature in °C
    """
    answer = (to_convert - 32) * 5 / 9
    return round_ans(answer)


def to_cad(to_convert):
    """
    Converts from °C to °F
    :param to_convert: Temperature to be converted in °C
    :return: Converted temperature in °F
    """
    answer = to_convert * 1.8 + 32
    return round_ans(answer)