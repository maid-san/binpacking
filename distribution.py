"""This is a module about distribution of items."""
import random

def dis_1(size):
    """
    1〜sizeまでのアイテムをランダムに返します。
    """
    return random.randint(1, size)

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

def dis_3(size):
    """
    常にサイズ size のアイテムを返します。
    """
    return size

def dis_4():
    """
    10%: 1, 10%: 3, 80%: 8 の確率でアイテムをそれぞれ返します。
    """
    prob = random.randint(1, 10)

    if 1 <= prob and prob < 2:
        return 1
    if 2 <= prob and prob < 3:
        return 3
    if 3 <= prob and prob <= 10:
        return 8

def dis_5():
    """
    5%: 1, 10%: 3, 85%: 6 の確率でアイテムをそれぞれ返します。
    """
    prob = random.randint(1, 100)

    if 1 <= prob and prob < 5:
        return 1
    if 5 <= prob and prob < 15:
        return 3
    if 15 <= prob and prob <= 100:
        return 8

def dis_6():
    """
    20%: 1, 20%: 3, 60%: 6 の確率でアイテムをそれぞれ返します。
    """
    prob = random.randint(1, 10)

    if 1 <= prob and prob < 3:
        return 1
    if 3 <= prob and prob < 5:
        return 3
    if 5 <= prob and prob <= 10:
        return 6


