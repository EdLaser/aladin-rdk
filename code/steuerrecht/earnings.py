from steuerrecht import dependecys

GEHALT = ["verdient als Mitarbieter"]

BETEILIGUNG = ["erhält durch Beteiligung"]

DIVIDENDE = ["bekommt eine Dividende i.H.v"]

VERMIETUNG = ["vermietet eine Wohnung, er verlangt"]

ALL = { "GEHALT": GEHALT, "BETEILIGUNG": BETEILIGUNG, "DIVIDENDE": DIVIDENDE, "VERMIETUNG": VERMIETUNG }

def set_params(char, number):
    arr = ""
    NUMBERS = dependecys.generate_number_dep()
    for key, value in ALL.items():
        arr += f"{char} {value[0]} {NUMBERS[key]}. "
    print(NUMBERS)
    return arr