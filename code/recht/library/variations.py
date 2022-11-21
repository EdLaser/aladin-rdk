import random
import torch

from library.nodepool.case import Case
from transformers import AutoModelForMaskedLM, AutoTokenizer, pipeline

tokenizer = AutoTokenizer.from_pretrained("bert-base-german-cased")
model = AutoModelForMaskedLM.from_pretrained("bert-base-german-cased")  # type: ignore


def multi_mask(text) -> str:
    import torch
    # text = "The capital of France [MASK] contains the Eiffel [MASK]."
    # Converts a string to a sequence of ids (integer), using the tokenizer and vocabulary.
    token_ids = tokenizer.encode(text, return_tensors='pt')

    token_ids_tk = tokenizer.tokenize(text, return_tensors='pt')

    masked_position = (token_ids.squeeze() == tokenizer.mask_token_id).nonzero()  # type: ignore

    masked_pos = [mask.item() for mask in masked_position ]

    with torch.no_grad():
        output = model(token_ids)

    last_hidden_state = output[0].squeeze()

    print ("\n")

    list_of_list =[]

    for mask_index in masked_pos:

        mask_hidden_state = last_hidden_state[mask_index]

        idx = torch.topk(mask_hidden_state, k=5, dim=0)[1]

        words = [tokenizer.decode(i.item()).strip() for i in idx]

        list_of_list.append(words)

    best_guess = ""
    # list of possible token replicas for each token
    for j in list_of_list:
        text = text.replace("[MASK]", j[0], 1)
        print(f"ELEM: {j} SENT: {text}")
        best_guess = best_guess+" "+j[0]

    return text


def build_variaton(case: Case) -> str:
    '''
    Build a random variation for the given case, with the help of mask filling.

    Parameters:
        case(Case): The case to generate the variation for.

    Returns:
       String containing the generated sentence.
    '''
    if case.object == 'Er' or case.object == 'Sie':
        pass
    if case.name == 'Abschreibung':
        return multi_mask(random.choice([
            f"[MASK] {case.object} {case.verb} {case.subject} [MASK] {case.number}€ [MASK].",
            f"{case.object} [MASK] {case.verb} {case.subject} [MASK] {case.number}€ [MASK].",
            f"[MASK] {case.verb} {case.object} {case.subject} [MASK] {case.number}€ [MASK].",
        ]))

    if case.name == 'Vermietung-WK':
        return multi_mask(random.choice([
            f"[MASK] {case.object} {case.verb} {case.subject} [MASK] {case.number}€ [MASK].",
            f"{case.object} [MASK] {case.verb} {case.subject} [MASK] {case.number}€ [MASK].",
            f"[MASK] {case.verb} {case.object} {case.subject} [MASK] {case.number}€ [MASK].",
        ]))

    if case.name == 'Gehalt-WK':
        return multi_mask(random.choice([
            f"[MASK] {case.object} {case.verb} {case.subject} [MASK] {case.number}€ [MASK].",
            f"{case.object} [MASK] {case.verb} {case.subject} [MASK] {case.number}€ [MASK].",
            f"[MASK] {case.verb} {case.object} {case.subject} [MASK] {case.number}€ [MASK].",
        ]))

    if case.name == 'Gehalt':
        return multi_mask(random.choice([
            f"[MASK] {case.subject} {case.verb} {case.object} {case.number}€.",
            f"{case.object} [MASK] {case.subject} [MASK] {case.verb} {case.number}€.",
            f"{case.object} {case.verb} [MASK] {case.subject} {case.number}€."
        ]))

    if case.name == 'Dividende':
        return multi_mask(random.choice([
            f"[MASK] {case.subject} {case.verb} {case.object} {case.number}€.",
            f"{case.object} {case.verb} [MASK] {case.subject} i.H.v {case.number}€.",
            f"[MASK] [MASK] {case.subject} {case.verb} {case.object} {case.number}€."
        ]))

    if case.name == 'Beteiligung':
        return multi_mask(random.choice([
            f"[MASK] {case.subject} {case.verb} {case.object} {case.number}€.",
            f"[MASK] {case.subject} [MASK] {case.verb} {case.object} {case.number}€.",
            f"[MASK] {case.object} {case.subject} hält {case.verb} [MASK] {case.number}€.",
        ]))

    if case.name == 'Vermietung':
        return multi_mask(random.choice([
            f"[MASK] {case.object} [MASK] {case.subject} {case.verb} [MASK] {case.object} {case.number}€.",
            f"{case.object} {case.verb} [MASK] {case.subject} [MASK] {case.number}€.",
            f"[MASK] {case.verb} {case.object} [MASK] {case.subject} [MASK] {case.number}€.",
        ]))

    return f"Generation failed. {str(case)}"
