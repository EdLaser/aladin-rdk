import random

from library.nodepool.case import Case
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-german-cased")
model = AutoModel.from_pretrained("dbmdz/bert-base-german-cased")


def test():

    TXT = "My friends are <mask> but they eat too many carbs."
    input_ids = tokenizer([TXT], return_tensors="pt")["input_ids"]
    logits = model(input_ids).logits

    masked_index = (input_ids[0] == tokenizer.mask_token_id).nonzero().item()
    probs = logits[0, masked_index].softmax(dim=0)
    values, predictions = probs.topk(5)

    tokenizer.decode(predictions).split()


def get_prediction(sent: str):
    token_ids = tokenizer.encode(sent, return_tensors='pt')
    masked_position = (token_ids.squeeze() ==
                       tokenizer.mask_token_id).nonzero()
    masked_pos = [mask.item() for mask in masked_position]

    with torch.no_grad():
        output = model(token_ids)  # type: ignore

    last_hidden_state = output[0].squeeze()

    list_of_list = []
    for index, mask_index in enumerate(masked_pos):
        mask_hidden_state = last_hidden_state[mask_index]
        idx = torch.topk(mask_hidden_state, k=5, dim=0)[1]
        words = [tokenizer.decode(i.item()).strip() for i in idx]
        list_of_list.append(words)
        print("Mask ", index+1, "Guesses : ", words)

    best_guess = ""
    for j in list_of_list:
        best_guess = best_guess+" "+j[0]

    return best_guess


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
        random.choice([
            f"Da {case.object} eine {case.subject} {case.verb} bezieht {case.object} {case.number}.",
            f"{case.object} {case.verb} eine {case.subject} und erwirtschaftet {case.number}.",
            f"Nebenbei {case.verb} {case.object} eine {case.subject} und verlangt {case.number}.",
        ])

    return "Generation failed."
