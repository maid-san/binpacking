from random import *

def dis_1():
    return randint(1, 10)

def dis_2():
    p = randint(1, 10)

    if 1 <= p and p < 2:
        return 1
    if 2 <= p and p < 3:
        return 3
    if 3 <= p and p <= 10:
        return 6 