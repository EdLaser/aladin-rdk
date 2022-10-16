from curses import erasechar
import random
from steuerrecht import earnings
from steuerrecht import numbers
import string

if __name__ == '__main__':
    task = ""
    char = random.choice(string.ascii_letters).upper()
    task = earnings.set_params(char, 3000)
   
    print(task)