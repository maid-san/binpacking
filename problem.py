"""This is a module solving various problems actually."""
import numpy as np
import pulp

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
