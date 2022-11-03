import random

def build_variatons(key, parts):
    variations = []

    if 'Werbungskosten' in key:
        wk_var = [
            f"{parts.get('Subject')} {parts.get('Verb')} {parts.get('Object')}"
        ]
        variations.append(random.choice(wk_var))
    if key == 'Gehalt':
        ge_var = [
            f"Als {parts.get('Subject')} {parts.get('Verb')} {parts.get('Object')} {parts.get('Number')}.",
            f"{parts.get('Object')} ist {parts.get('Subject')} und {parts.get('Verb')} {parts.get('Number')}.",
            f"{parts.get('Object')} {parts.get('Verb')} als {parts.get('Subject')} {parts.get('Number')}."
        ]
        variations.append(random.choice(ge_var))

    if key == 'Dividende':
        di_var = [
            f"Durch eine {parts.get('Subject')} {parts.get('Verb')} {parts.get('Object')} {parts.get('Number')}.",
            f"{parts.get('Object')} {parts.get('Verb')} eine {parts.get('Subject')} i.H.v {parts.get('Number')}.",
        ]
        variations.append(random.choice(di_var))

    if key == 'Beteiligung':
        be_var = [
            f"Aufgrund einer {parts.get('Subject')} {parts.get('Verb')} {parts.get('Object')} {parts.get('Number')}.",
            f"Durch eine {parts.get('Subject')} {parts.get('Verb')} {parts.get('Object')} {parts.get('Number')}.",
        ]
        variations.append(random.choice(be_var))

    if key == 'Vermietung':
        ve_var = [
            f"Da {parts.get('Object')} eine {parts.get('Subject')} {parts.get('Verb')} bezieht {parts.get('Object')} {parts.get('Number')}.",
            f"{parts.get('Object')} {parts.get('Verb')} eine {parts.get('Subject')} und erwirtschaftet {parts.get('Number')}.",
            f"Nebenbei {parts.get('Verb')} {parts.get('Object')} eine {parts.get('Subject')} und verlangt {parts.get('Number')}.",
        ]
        variations.append(random.choice(ve_var))

    return variations