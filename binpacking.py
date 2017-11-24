import time
import numpy as np
import argparse
from random import *
from decimal import *
from problem import binpacking_dual, zero_one_knapsack, binpacking

start = time.time()

seed(1998031713322)

parser = argparse.ArgumentParser(description = 'Solver of Binpacking Problem.')
parser.add_argument('-b', '--binsize', type=int, help='Bin Size')
parser.add_argument('-n', '--nitem', type=int, help='Number of Item')
args = parser.parse_args()

print(args)

BinSize = args.binsize
NumberOfItem = args.nitem

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