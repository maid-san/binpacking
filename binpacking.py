import time
import numpy as np
from random import *
from decimal import *
from problem import binpacking_dual, zero_one_knapsack, binpacking

seed(1998031713322)
start = time.time()
BinSize = 10
NumberOfItem = 100

item_list = []
for i in range(1, NumberOfItem):
    r = int(randint(1, BinSize))

    r = 1 if r < 1 else BinSize if r > BinSize else r
    item_list.append(r)

print("Bin Size: " + str(BinSize))
print("Number of Item: " + str(NumberOfItem))
print("Item List: " + str(item_list))

i = 1
a = np.array([[]])
while True:
    y = binpacking_dual(BinSize, item_list, a)
    mat = zero_one_knapsack(BinSize, item_list, y)

    if (mat * y.T)[0, 0] > 1:
        a = np.array(mat) if i == 1 else np.append(a, mat, axis=0)
    else:
        break

    i += 1

constraint = np.identity(len(item_list)).T if a.size == 0 else np.append(np.identity(len(item_list)), a, axis=0).T
binpacking(constraint)

print("i = " + str(i))
print("Time = " + str(time.time() - start) + "[sec]")