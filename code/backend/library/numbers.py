import random


def round_to_base(number, base):
    return base * round(number/base)


GEHALT = round_to_base(random.randrange(3000, 10000), 100)

BETEILIGUNG = round_to_base(random.randrange(10000, 30000), 1000)

DIVIDENDE = round_to_base(random.randrange(50000, 100000), 1000)

VERMIETUNG = round_to_base(random.randrange(500, 2000), 50)

WERBUNGSKOSTEN = round_to_base(random.randrange(100, 2000), 50)

ALL = {"Gehalt": GEHALT, "Beteiligung": BETEILIGUNG,
       "Dividende": DIVIDENDE, "Vermietung": VERMIETUNG,
       "Werbungskosten": WERBUNGSKOSTEN}
