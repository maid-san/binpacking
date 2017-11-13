import pulp
problem = pulp.LpProblem('TEMP-1', pulp.LpMinimize)

x1 = pulp.LpVariable('x1', 0, 1, 'Binary')
x2 = pulp.LpVariable('x2', 0, 1, 'Binary')
x3 = pulp.LpVariable('x3', 0, 1, 'Binary')
x4 = pulp.LpVariable('x4', 0, 1, 'Binary')
x5 = pulp.LpVariable('x5', 0, 1, 'Binary')
x6 = pulp.LpVariable('x6', 0, 1, 'Binary')

problem += x1 + x2 + x3 + x4 + x5 + x6

problem += x1 + x4 + x5 >= 1
problem += x2 + x4 + x6 >= 1
problem += x3 + x5 + x6 >= 1

problem += x1 >= 0
problem += x2 >= 0
problem += x3 >= 0
problem += x4 >= 0
problem += x5 >= 0
problem += x6 >= 0

print(problem)
problem.solve()

print("x1", x1.value());
print("x2", x2.value());
print("x3", x3.value());
print("x4", x4.value());
print("x5", x5.value());
print("x6", x6.value());
