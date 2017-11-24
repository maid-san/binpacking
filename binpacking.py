import time
import numpy as np
from random import *
from decimal import *
from problem import binpacking_dual, zero_one_knapsack, binpacking

start = time.time()
B = 100
s = []
for i in range(1, 4):
    r = int(normalvariate(4, 2))
    r = 1 if r < 1 else B if r > B else r
    s.append(r)

a = np.array([[]])

print("Bin size = " + str(B))
print("Item list = " + str(s))

i = 1
while True:
    y = binpacking_dual(B, s, a)
    mat = zero_one_knapsack(B, s, y)

    print("i = " + str(i))

    if (mat * y.T)[0, 0] > 1:
        a = np.array(mat) if i == 1 else np.append(a, mat, axis=0)
    else:
        break

    i += 1

constraint = np.identity(len(s)).T if a.size == 0 else np.append(np.identity(len(s)), a, axis=0).T
print("Time = " + str(time.time() - start) + "[sec]")