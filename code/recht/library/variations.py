import random
import torch

from library.nodepool.case import Case
from transformers import AutoModelForMaskedLM, AutoTokenizer, pipeline

tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-german-cased")
model = AutoModelForMaskedLM.from_pretrained("dbmdz/bert-base-german-cased")


def test_multi_mask(text):
    import torch

    # Converts a string to a sequence of ids (integer), using the tokenizer and vocabulary.
    token_ids = tokenizer.encode(text, return_tensors='pt')

    token_ids_tk = tokenizer.tokenize(text, return_tensors='pt')

    masked_position = (token_ids.squeeze() == tokenizer.mask_token_id).nonzero()  # type: ignore

    masked_pos = [mask.item() for mask in masked_position ]

    print (f"Masked Pos: {masked_pos}")

    with torch.no_grad():
        output = model(token_ids)

    last_hidden_state = output[0].squeeze()

    print ("Sentence : ",text)

    print ("\n")

    list_of_list =[]

    for mask_index in masked_pos:

        mask_hidden_state = last_hidden_state[mask_index]

        idx = torch.topk(mask_hidden_state, k=5, dim=0)[1]

        words = [tokenizer.decode(i.item()).strip() for i in idx]

        list_of_list.append(words)

        print (words)


    best_guess = ""

    for j in list_of_list:
        best_guess = best_guess+" "+j[0]
    
    print(f"Best gues: {best_guess}")


def test(text):
    text = "Er [MASK] Geschäftsführer [MASK] verdient 8000€."
    
    inputs = tokenizer(text, return_tensors="pt")
    token_logits = model(**inputs).logits
    # Find the location of [MASK] and extract its logits
    mask_token_index = torch.where(inputs["input_ids"] == tokenizer.mask_token_id)[1]  # type: ignore
    mask_token_logits = token_logits[0, mask_token_index, :]
    # Pick the [MASK] candidates with the highest logits
    top_5_tokens = torch.topk(mask_token_logits, 3, dim=1).indices[0].tolist()
    var_list = []
    for token in top_5_tokens:
        var_list.append(
            f"'{text.replace(tokenizer.mask_token, tokenizer.decode([token]))}'")

    return var_list


def build_variaton(case: Case) -> str:
    '''
    Build a random variation for the given case.

    Parameters:
        case(Case): The case to generate the variation for.
        parts()

    Returns:
       String containing the generated sentence.
    '''

    if case.name == 'Werbungskosten':
        return random.choice([
            f"{case.object} {case.verb} {case.subject}"
        ])

    if case.name == 'Gehalt':
        return random.choice([
            f"Als {case.subject} {case.verb} {case.object} {case.number}.",
            f"{case.object} ist {case.subject} und {case.verb} {case.object}.",
            f"{case.object} {case.verb} als {case.subject} {case.number}."
        ])

    if case.name == 'Dividende':
        return random.choice([
            f"Durch eine {case.subject} {case.verb} {case.object} {case.number}.",
            f"{case.object} {case.verb} eine {case.subject} i.H.v {case.number}.",
        ])

    if case.name == 'Beteiligung':
        return random.choice([
            f"Aufgrund einer {case.subject} {case.verb} {case.object} {case.number}.",
            f"Durch eine {case.subject} {case.verb} {case.object} {case.number}.",
        ])

    if case.name == 'Vermietung':
        return random.choice([
            f"Da {case.object} eine {case.subject} {case.verb} bezieht {case.object} {case.number}.",
            f"{case.object} {case.verb} eine {case.subject} und erwirtschaftet {case.number}.",
            f"Nebenbei {case.verb} {case.object} eine {case.subject} und verlangt {case.number}.",
        ])

    return "Generation failed."
