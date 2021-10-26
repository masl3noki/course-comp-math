import sympy as sp
#import numpy as np
#from lambdify import *
from sympy.core.rules import Transform


print("TEST MASLO")
#t = np.var('t')
t = sp.symbols('t')


#precision = 10**-3
#STOP = 15 #верхний предел шага


def comp_sin():
    y = sp.sin(t)
    return y


def comp_exp():
    y = sp.exp(t)
    return y


def mac_series(n, u):
    u_ = sp.lambdify(t, u) #"готовая" func(t) для numpy.var
    sum = u_(0) #первый член разложения по маклорену

    #try: #assert на n, если optimal_n выдаст внезапно n<=0
    if n == 0:
        return sum
    else:
        i = 1
        while i <= n:
            u = sp.diff(u, t) # очищается из памяти прошлое значение u, теперь u указывает на производную du/dt
            u_ = sp.lambdify(t, u) # аналогично
            sum = sum + (u_(0) * (t ** i)) / sp.factorial(i)
            i += 1
        return sum
    #except (0):

n = int(input("f=sin(x). Введите n: "))

expr = mac_series(n, comp_sin())
'''
expr_round = expr
for a in sp.preorder_traversal(expr):
    if isinstance(a, float):
        expr_round = expr_round.subs(a, round(a, 3))
'''

print('sin(t):\n',
      'На отрезке [0; 1]: ', expr, '\n',
      'На отрезке [10; 11]: ', '\n') #TODO сделать для отрезка (подставить t-10 в синус)

n = int(input("f=exp(x). Введите n: "))

print('exp(t):\n',
      'На отрезке [0; 1]: ', mac_series(n, comp_exp()), '\n',
      'На отрезке [10; 11]: ', '\n') #TODO сделать для отрезка (подставить t-10 в exp)

'''''
def optimal_n(u_, i):
#TODO оценить остаточный член так, чтобы он был меньше точности

    check = ((sp.diff(u_, t) * t**(i+1)) / sp.factorial(i+1)) #остаточный член ряда Маклорена в форме Лагранжа
    if check(1) <= precision:
        return i, True
    else:
        return -1, False


def mac_series(u): #u = func1 или func2

    u_ = sp.lambdify(t, u) #"готовая" func(t) для numpy.var
    sum = u_(0) #первый член разложения по маклорену
    i = 1

    while True:
        u = sp.diff(u, t)  # очищается из памяти прошлое значение u, теперь u указывает на производную du/dt
        u_ = sp.lambdify(t, u)  # аналогично
        sum = sum + ((u_(0) * (t ** i)) / sp.factorial(i))
        if optimal_n(u_, i)[2]:
            return sum, i
        i += 1
        if i >= STOP:
            break
'''''