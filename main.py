import time
import numpy as np
import argparse
from random import *
from decimal import *
from distribution import *
from problem import binpacking_dual, zero_one_knapsack, binpacking

start = time.time()

seed(1998031713322)

parser = argparse.ArgumentParser(description = 'Solver of Binpacking Problem.')
parser.add_argument('-b', '--binsize', type=int, help='Bin Size')
parser.add_argument('-n', '--nitem', type=int, help='Number of Item')
args = parser.parse_args()

BinSize = args.binsize
NumberOfItem = args.nitem

item_list = []
for i in range(1, NumberOfItem):
    r = dis_2()
    item_list.append(r)

print("Bin Size: " + str(BinSize))
print("Item List: " + str(item_list))

i = 1
a = np.array([[]])
while True:
    print("# TEMP-" + str(i))
    y = binpacking_dual(BinSize, item_list, a)
    mat = zero_one_knapsack(BinSize, item_list, y)

    if (mat * y.T)[0, 0] > 1:
        a = np.array(mat) if i == 1 else np.append(a, mat, axis=0)
    else:
        break

    print(a)

    i += 1

constraint = np.identity(len(item_list)).T if a.size == 0 else np.append(np.identity(len(item_list)), a, axis=0).T
answer = binpacking(constraint)

print("# MAIN PROBLEM")
print(constraint)
print(answer)

print("i = " + str(i))
print("n = " + str(NumberOfItem) + ", time = " + str(time.time() - start))