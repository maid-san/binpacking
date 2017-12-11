"""This is a module about distribution of items."""
import random

def dis_1():
    """
    1〜10までのアイテムをランダムに返します。
    """
    return random.randint(1, 10)

def dis_2():
    """
    10%: 1, 10%: 3, 80%: 6 の確率でアイテムをそれぞれ返します。
    """
    prob = random.randint(1, 10)

    if 1 <= prob and prob < 2:
        return 1
    if 2 <= prob and prob < 3:
        return 3
    if 3 <= prob and prob <= 10:
        return 6 
    