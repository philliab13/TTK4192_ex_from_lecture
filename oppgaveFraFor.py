from casadi import *
import numpy as np

x=1.2
y=0.6
theta=0
gam=1

# Symbols/expressions
v = MX.sym('v')
w = MX.sym('w')
f = (v-1)**2+w**2
g = 2*(x-2)*v*np.cos(theta)+2*y*v*np.sin(theta)+gam*((x-2)**2+y**2-1)

nlp = {}                 # NLP declaration
nlp['x']= vertcat(v,w) # decision vars
nlp['f'] = f             # objective
nlp['g'] = g             # constraints

# Create solver instance
F = nlpsol('F','ipopt',nlp)

# Solve the problem using a guess
sol = F(lbg=0, ubg=inf)

print("-----")
print("objective at solution = ", sol["f"])
print("primal solution = ", sol["x"])