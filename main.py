"""
This is a solver of binpacking problem.
"""
import time
import random
import argparse
import numpy as np
from distribution import dis_1, dis_2
from problem import binpacking_dual, zero_one_knapsack, binpacking

def get_item_size(dis):
    """
    This is a function returning size of an item.
    """
    if dis == 1:
        return dis_1()
    if dis == 2:
        return dis_2()
    else:
        raise IndexError

START = time.time()
random.seed(1998031713322)
PARSER = argparse.ArgumentParser(description='Solver of Binpacking Problem.')
PARSER.add_argument('-b', '--binsize', type=int, help='Bin Size')
PARSER.add_argument('-n', '--nitem', type=int, help='Number of Item')
PARSER.add_argument('-d', '--distribution', type=int, help='Item distribution')
ARGS = PARSER.parse_args()

BIN_SIZE = ARGS.binsize
NUMBER_OF_ITEM = ARGS.nitem

ITEM_LIST = []
for i in range(1, NUMBER_OF_ITEM + 1):
    r = dis_2()
    ITEM_LIST.append(r)

print("Bin Size: " + str(BIN_SIZE))
print("Item List: " + str(ITEM_LIST))

i = 1
constraints = np.array([[]])
while True:
    print("# TEMP-" + str(i))
    y = binpacking_dual(BIN_SIZE, ITEM_LIST, constraints)
    a = zero_one_knapsack(BIN_SIZE, ITEM_LIST, y)

    print((a * y.T)[0, 0])
    if (a * y.T)[0, 0] > 1.00000001:
        constraints = np.append(constraints, a, axis=0) if i != 1 else np.array(a)
    else:
        break
    print(constraints)

    i += 1

CONSTRAINT = np.identity(len(ITEM_LIST)).T if constraints.size == 0 \
                else np.append(np.identity(len(ITEM_LIST)), constraints, axis=0).T
ANSWER = binpacking(CONSTRAINT)

print("# MAIN PROBLEM")
print(CONSTRAINT)
print(ANSWER)

print("i = " + str(i))
print("n = " + str(NUMBER_OF_ITEM) + ", time = " + str(time.time() - START))
