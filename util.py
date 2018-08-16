from math import floor


def suffix(n):
    ones = n % 10
    tens = n % 100
    if tens == 11 or tens == 12 or tens == 13:
        return 'th'
    elif ones == 1:
        return 'st'
    elif ones == 2:
        return 'nd'
    elif ones == 3:
        return 'rd'
    else:
        return 'th'


# just for fun
def ordinal(n):
    return "%d%s" % (
        n,
        "tsnrhtdd"[(floor(n / 10) % 10 != 1) * (n % 10 < 4) * n % 10::4]
    )
