from steuerrecht import earnings, spendings, numbers

def generate_number_dep():
    NUMBERS = {}
    for earn in earnings.ALL:
        for key, num in numbers.ALL.items():
            if earn is key:
                NUMBERS[earn] = num
            else:
                pass
    print(NUMBERS)
    return NUMBERS
