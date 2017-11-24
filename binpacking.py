import time
import random
import argparse
import numpy as np
from decimal import *
from problem import binpacking_dual, zero_one_knapsack, binpacking

start = time.time()
B = 8
s = []
for i in range(1, 4):
    r = int(np.random.normal(4, 2))
    r = 1 if r < 1 else B if r > B else r
    s.append(r)

a = np.array([[]])

# print("## Parameter:")
print("Bin size = " + str(B))
print("Item list = " + str(s))
# print("\n## Dual Problem:")

i = 1
while True:
    y = binpacking_dual(B, s, a)
    mat = zero_one_knapsack(B, s, y)

    print("i = " + str(i))
    #print("binpacking: " + str(y))
    #print("0-1 knapsack: " + str(mat))

    if (mat * y.T)[0, 0] > 1:
        a = np.array(mat) if i == 1 else np.append(a, mat, axis=0)
    else:
        break

    i += 1

constraint = np.identity(len(s)).T if a.size == 0 else np.append(np.identity(len(s)), a, axis=0).T

# print("\n## Main Problem:")
# print("constraint: ")
# print(constraint)
# print(binpacking(constraint))
# print("Count: " + str(i))
print("Time = " + str(time.time() - start) + "[sec]")
