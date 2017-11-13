import pulp
problem = pulp.LpProblem('TEMP-1', pulp.LpMaximize)

y1 = pulp.LpVariable('y1', 0, 1, 'Continuous')
y2 = pulp.LpVariable('y2', 0, 1, 'Continuous')
y3 = pulp.LpVariable('y3', 0, 1, 'Continuous')

problem += y1 + y2 + y3

problem += y1 <= 1
problem += y2 <= 1
problem += y3 <= 1
problem += y1 + y2 <= 1
problem += y1 + y3 <= 1
problem += y2 + y3 <= 1

problem += y1 >= 0
problem += y2 >= 0
problem += y3 >= 0

print(problem)

problem.solve()

print(problem.status)
print("y1", y1.value());
print("y2", y2.value());
print("y3", y3.value());
