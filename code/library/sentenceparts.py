
# Regex sollte klappen
NOUNS = ["Er", "Sie"]

CONJUNCTIONS = [
    'Als',
    'Zusätzlich',
    'Nebenbei',
    'Außerdem'
]

VERBS = ['verdient', 'erhält', 'bekommt']

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
