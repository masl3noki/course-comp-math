import math as m
import numpy as np


def func1(x):
    return lambda x: m.exp(x**2) / (2 * m.sqrt(2 * m.e))


def func2(x):
    return lambda x: m.sqrt(m.log(2 * x * m.sqrt(2 * m.e)))


def sim(x, method): #итерации
    if abs(method(x) - x) < precision / 2:
        return x
    return sim(method(x), method)

#def local:
        #TODO: сделать локализацию в виде функции


precision = 1e-3
#p = pow(precision, ) #точное округление
roots = []
print("Нахождение полуширины функции")
h = float(input("Введите оптимальное количество шага (шаг <= 1): "))


f = lambda x: x * m.exp(-x**2) - (1 / (2 * m.sqrt(2 * m.e))) #y_3

#Локализация корней (ака x*)
for x in np.arange(0, 2, h):
    if (f(x) * f(x+h)) <= 0:
        roots.append(x)


solution1 = sim(
                roots[0], func1(x)
                )
solution2 = sim(
                roots[1], func2(x)
                )

print("Найдены следующие корни:\n",
      "x1 =", round(solution1, 3), "\n",
      "x2 =", round(solution2, 3)
      )

print("Полуширина функции при x>=0:", round(abs(solution2 - solution1), 3))