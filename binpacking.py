import numpy as np
import sys
import pulp
import time
import random
import argparse


def binpacking_dual(B, s, a):
    problem = pulp.LpProblem('binpacking-dual', pulp.LpMaximize)

    y = np.array([])
    for i in range(0, len(s)):
        y = np.append(y, pulp.LpVariable('y' + str(i), 0, 1, 'Continuous'))
    y = np.asmatrix(y.reshape(len(s), 1))

    c = np.ones((1, len(s)))
    cy = c * y

    problem += cy[0, 0]

    A = np.asarray(np.identity(len(s)))

    if a != [[]]:
        A = np.append(A, a, axis=0)
    A = np.asmatrix(A)

    Ay = A * y

    for i in Ay:
        problem += i[0, 0] <= 1

    problem.solve()

    ret = np.array([])
    for i in y:
        ret = np.append(ret, i[0, 0].value())

    return np.asmatrix(ret.reshape(1, len(s)))

def zero_one_knapsack(B, s, y):
    problem = pulp.LpProblem('0-1-knapsack', pulp.LpMaximize)

    a = np.array([])
    for i in range(0, len(s)):
        a = np.append(a, pulp.LpVariable('a' + str(i), 0, 1, 'Binary'))
    a = np.asmatrix(a.reshape(len(s), 1))

    ya = y * a

    problem += ya[0, 0]

    s = np.append([], s).reshape(1, len(s))
    sa = s * a

    problem += sa[0, 0] <= B

    problem.solve()

    ret = np.array([])
    for i in a:
        ret = np.append(ret, i[0, 0].value())

    return np.asmatrix(ret.reshape(1, len(ret)))

def binpacking(a):
    problem = pulp.LpProblem('binpacking', pulp.LpMinimize)

    x = np.array([])
    for i in range(0, a[0].size):
        x = np.append(x, pulp.LpVariable('x' + str(i), 0, 1, 'Continuous'))
    x = np.asmatrix(x.reshape(a[0].size, 1))

    c = np.ones((1, a[0].size))
    cx = c * x

    problem += cx[0, 0]

    Ax = a * x
    for i in Ax:
        problem += i[0, 0] >= 1

    problem.solve()

    ret = np.array([])
    for i in x:
        ret = np.append(ret, i[0, 0].value())

    return np.asmatrix(ret.reshape(1, a[0].size))

parser = argparse.ArgumentParser(description="hogehoge")
parser.add_argument("--size", "-s", type=int, required=True)
parser.add_argument("--nitem", "-n", type=int, required=True)
parser.add_argument("--min", "-m", type=int, required=True)
args = parser.parse_args()

start = time.time()
B = args.size
s = []
for i in range(0, args.nitem):
    s.append(random.randint(args.min, B - 1))

a = np.array([[]])
print("Bin size: " + str(B))
print("Item list: " + str(s))
i = 1

while True:
    print("### TEMP-" + str(i))
    y = binpacking_dual(B, s, a)
    mat = zero_one_knapsack(B, s, y)
    print("binpacking: " + str(y))
    print("0-1 knapsack: " + str(mat))

    if (mat * y.T)[0, 0] > 1:
        if i == 1:
            a = np.array(mat)
        else:
            a = np.append(a, mat, axis=0)
    else:
        break

    print("constraint: ")
    print(str(np.append(np.identity(len(s)), a, axis=0).T) + "\n")

    i += 1

print("\n主問題: ")
print("constraint: ")
if a.size == 0:
    constraint = np.identity(len(s))
else:
    constraint = np.append(np.identity(len(s)), a, axis=0).T
print(constraint)
print(binpacking(constraint))

print("\n実行回数: " + str(i))
print("実行時間: " + str(time.time() - start))
