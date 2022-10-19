import dependecys
import sentenceparts
import random

GEHALT = {1: "verdient als Mitarbieter",
          2: "erhält als Geschäftsführer ein Gehalt von",
          3: "bekommt pro Monat"}

BETEILIGUNG = {1: "erhält durch Beteiligung"}

DIVIDENDE = {1: "bekommt eine Dividende i.H.v"}

VERMIETUNG = {1: "vermietet eine Wohnung, er verlangt"}

ALL = { "GEHALT": GEHALT, "BETEILIGUNG": BETEILIGUNG, "DIVIDENDE": DIVIDENDE, "VERMIETUNG": VERMIETUNG }


def set_params(char):
    arr = ""
    numbers = dependecys.generate_number_dep()
    for key, value in ALL.items():
        arr += f"{char} {random.choice(value)} {numbers[key]}. "
    return arr
