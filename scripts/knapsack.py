import pulp
problem = pulp.LpProblem('knapsack', pulp.LpMaximize)

a1 = pulp.LpVariable('a1', 0, 1, 'Binary')
a2 = pulp.LpVariable('a2', 0, 1, 'Binary')
a3 = pulp.LpVariable('a3', 0, 1, 'Binary')

problem += 0.5*a1 + 0.5*a2 + 0.5*a3
problem += 3*a1 + 3*a2 + 3*a3 <= 8

problem.solve()

print(problem.status)
print("a1", a1.value());
print("a2", a2.value());
print("a3", a3.value());

