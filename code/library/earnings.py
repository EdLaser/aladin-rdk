import dependecys
import sentenceparts
import random

GEHALT = ["verdient als Mitarbieter", "erhält als Geschäftsführer ein Gehalt von", "bekommt pro Monat"]

BETEILIGUNG = ["erhält durch Beteiligung", ""]

DIVIDENDE = ["bekommt eine Dividende i.H.v", ""]

VERMIETUNG = ["vermietet eine Wohnung, er verlangt"]

ALL = { "GEHALT": GEHALT, "BETEILIGUNG": BETEILIGUNG, "DIVIDENDE": DIVIDENDE, "VERMIETUNG": VERMIETUNG }


def set_params(char):
    arr = ""
    numbers = dependecys.generate_number_dep()
    for key, value in ALL.items():
        arr += f"{char} {random.choice(value)} {numbers[key]}. "
    return arr
