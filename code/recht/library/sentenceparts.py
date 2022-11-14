
# Regex sollte klappen
NOUNS = ["Er", "Sie"]

CONJUNCTIONS = {
    'Gehalt': ['Als'],
    'Dividende': 'Zusätzlich',
    'Vermietung': 'Nebenbei',
    'Beteiligung': 'Außerdem'
}

VERBS = {'Gehalt': ['verdient', 'erhält', 'bekommt'],
         'Beteiligung': ['erhält', 'bekommt'],
         'Dividende': ['erhält', 'bekommt'],
         'Vermietung': ['vermietet'],
         'Abschreibung': ['setzt'],
         'Gehalt-WK': ['kauft', 'meldet', 'zahlt'],
         'Vermietung-WK': ['setzt', 'meldet']
         }

GEHALT_PROFESSIONS = [
    {'Er': 'Mitarbeiter', 'Sie': 'Mitarbeiterin'},
    {'Er': 'Geschäftsführer', 'Sie': 'Geschäftsführerin'},
    {'Er': 'Angestellter', 'Sie': 'Angestellte'},
    {'Er': 'Arbeitnehmer', 'Sie': 'Arbeitnehmerin'}
]

BETEILIGUNG_VARIATIONS = [
    'Beteiligung', 'Kapitalbeteiligung', 'Unternehmensbeteiligung'
]

DIVIDENDE = ['Dividende']

VERMIETUNG_OBJECTS = [
    'Wohnung', 'Apartment', 'Unterkunft', 'Lagerhalle'
]

ABSCHREIBUNG = ["Abschreibungen"]

GEHALT_WK = [
    'Arbeitsmittel', 'Reisekosten', 'Arbeitszimmer', 'Fahrtkosten',
    'Fachbücher', 'Bekleidung', 'Notebook', 'Telefonkosten',
    'Smartphone',
]

VERMIETUNG_WK = [
    'Grundsteuer', 'Heizkosten', 'Finanzierungskosten',
    'Kabelanschluss', 'Verwaltungskosten', 'Kosten für Entwässerung'
]

EARNINGS = {
    'Gehalt': GEHALT_PROFESSIONS,
    'Beteiligung': BETEILIGUNG_VARIATIONS,
    'Dividende': DIVIDENDE,
    'Vermietung': VERMIETUNG_OBJECTS
}

SPENDINGS = {
    'Gehalt-WK': GEHALT_WK,
    'Vermietung-WK': VERMIETUNG_WK,
    'Abschreibung': ABSCHREIBUNG
}
