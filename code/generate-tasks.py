import random
import earnings
import numbers
import string

if __name__ == '__main__':
    char = random.choice(string.ascii_letters).upper()
    task = earnings.set_params(char)

    print(task)