from library import dependencys
from library import sentenceparts
import random

GEHALT = {1: "verdient als Mitarbieter",
          2: "erhält als Geschäftsführer ein Gehalt von",
          3: "bekommt pro Monat"}

BETEILIGUNG = {1: "erhält durch Beteiligung"}

DIVIDENDE = {1: "bekommt eine Dividende i.H.v"}

VERMIETUNG = {1: "vermietet eine Wohnung, er verlangt"}

ALL = {"GEHALT": GEHALT, "BETEILIGUNG": BETEILIGUNG, "DIVIDENDE": DIVIDENDE, "VERMIETUNG": VERMIETUNG}
