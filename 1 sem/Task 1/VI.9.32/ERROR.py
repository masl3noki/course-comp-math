import sympy as sp
import numpy as np

x = [1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]
y = [92228496, 106021537, 123202624, 132164569, 151325798, 179323175, 203211926, 226545805, 248709873, 281421906]
X = np.zeros(len(x))

def split_diff(x, y):
    Fx = np.zeros((len(x), len(y)))
    for i in range(0, len(y)-1):
        Fx[0][i] = y[i]
    for j in range(1, len(x)-1):
        for i in range(0, len(y)-j-1):
            X[j-1] = x[j-1]-x[i+j]
        for i in range(0, len(y)-1):
            F = Fx[]
    print(Fx)

split_diff(x, y)
