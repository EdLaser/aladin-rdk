import random

GEHALT = {
    "COMB_1": 
        [
            "verdient als Mitarbieter",
            "erhält als Geschäftsführer ein Gehalt von",
            "bekommt pro Monat"
        ],
    "COMB_2": 
        [
            "Als Mitarbeiter verdient",
            "Als Geschäftsführer verdient"
            "Die Entlohnung von"
        ],
}

BETEILIGUNG = {
    "COMB_1": ["erhält durch Beteiligung", "verdient durch Beteiligung"],
    "COMB_2": ["Durch seine Beteiligung bekommt" ],
}

DIVIDENDE = {
    "COMB_1": ["bekommt eine Dividende i.H.v"],
    "COMB_2": [""]
}

VERMIETUNG = ["vermietet eine Wohnung, er verlangt"]

ALL = {"GEHALT": GEHALT, "BETEILIGUNG": BETEILIGUNG, "DIVIDENDE": DIVIDENDE, "VERMIETUNG": VERMIETUNG}
