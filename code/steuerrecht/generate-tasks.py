from curses import erasechar
import random
from steuerrecht import earnings
from steuerrecht import numbers
import string

if __name__ == '__main__':
    char = random.choice(string.ascii_letters).upper()
    task = earnings.set_params(char)
   
    print(task)