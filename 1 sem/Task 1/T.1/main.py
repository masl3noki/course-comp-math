import math as m
#import sympy as sp
import numpy as np

print("TEST MASLO")

'''
x = sp.symbols('x')
y = sp.symbols('y')
def eq1(x,y):
    f = x**2 + y**2 - 1
    return f

def eq2(x,y):
    f = y - math.tan(x)
    return f
'''

def eq1(x,y):
    return x**2 + y**2 - 1

def eq2(x,y):
    return y - m.tan(x)

def corr(Ai):
    #матричное произведение обратной матрицы Якобиана J на F(u_k) для формулы u_k+1=u_k+J^-1*F(u_k)
    return np.linalg.inv(J(*Ai)) @ F(*Ai)

def Newton(A0):
    A1 = A0.copy()
    A2 = A1 - corr(A1)
    while True:
        if abs(A2-A1).any() < precision:
            break
        A1 = A2.copy()
        A2 = A2 - corr(A2)
    return A2

print("Решить графически с точностью 10**-6: \n",
      "         x**2+y**2=1\n",
      "         y=tan(x)\n")

precision = 10**-6

F = lambda x, y: [eq1(x, y), eq2(x, y)] # матрица F
J = lambda x, y: np.array([
                           [2*x, 2*y],
                           [-1 / (m.cos(x)**2), 1]
                           ]) # якобиан


print("Первый корень считаем от точки A=[ 1 ; 1 ]: \n",
      "A_root=[", round(Newton(np.array([1, 1]))[0], 6), ";", round(Newton(np.array([1, 1]))[1], 6), "]\n")
print("Второй корень считаем от точки B=[ -1 ; -1 ]: \n",
      "B_root=[", round(Newton(np.array([-1, -1]))[0], 6), ";", round(Newton(np.array([-1, -1]))[1], 6), "]\n")