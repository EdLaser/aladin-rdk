from steuerrecht import earnings, spendings, numbers

def generate_number_dep():
    numbers = {}
    for earn in earnings.ALL:
        for key, num in numbers.ALL.items():
            if earn is key:
                numbers[earn] = num
            else:
                pass
    return NUMBERS
