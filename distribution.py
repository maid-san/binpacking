"""This is a module about distribution of items."""
import random

def dis_1():
    return random.randint(1, 10)

def dis_2():
    prob = random.randint(1, 10)

    if 1 <= prob and prob < 2:
        return 1
    if 2 <= prob and prob < 3:
        return 3
    if 3 <= prob and prob <= 10:
        return 6 
    