
# Regex sollte klappen
NOUNS = ["Er", "Sie"]

CONJUNCTIONS = {
    'Gehalt': ['Als'],
    'Dividende':'Zusätzlich',
    'Vermietung':'Nebenbei',
    'Beteiligung':'Außerdem'
}

VERBS = {'Gehalt': ['verdient', 'erhält', 'bekommt'],
         'Beteiligung': ['erhält', 'bekommt'],
         'Dividende': ['erhält', 'bekommt'],
         'Vermietung': ['vermietet']
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

ALL = {
    'Gehalt': GEHALT_PROFESSIONS,
    'Beteiligung': BETEILIGUNG_VARIATIONS,
    'Dividende': DIVIDENDE,
    'Vermietung': VERMIETUNG_OBJECTS
}
