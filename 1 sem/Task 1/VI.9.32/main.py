import sympy as sp

x = [1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]
y = [92228496, 106021537, 123202624, 132164569, 151325798, 179323175, 203211926, 226545805, 248709873, 281421906]

def Newton(x, y):
   if len(x) == 1:
        #print(d[x[0]])
        return d[x[0]]
   return (Newton(x[1:], y) - Newton(x[: len(x) - 1], y)) / (x[len(x) - 1] - x[0])

X = sp.symbols('X')

d = dict(zip(x, y))
P = 0
n = 1

for i in range(len(x)):
    P = P + n * Newton(x[0:i + 1], y)
    n = n * (X - x[i])
print('Interpolant: ',sp.simplify(P))

pn = sp.lambdify(X, P, "numpy")

y_new = [0] * len(x)

for i in range(len(x)):
    y_new[i] = pn(x[i])

y_a = pn(2010)
print(y_a)
print('2010: ', (y_a / 308745538)*100, ' %') 

