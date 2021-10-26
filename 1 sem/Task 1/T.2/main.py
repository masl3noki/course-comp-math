import math as m
import numpy as np
import sympy as sp


def func(x):
    return m.sin(100 * x) * m.exp(-x ** 2) * m.cos(2 * x)


def x1(start, finish, N, i): #размечаем равномерную сетку, параметризируем x=x(i)
    return start + (finish - start) * i / (2 * N)


def simpson(f, start, finish, N):
    funcs = [] #значения на узлах сетки. В цикле их заполняем.

    for i in range(0, 2 * N + 1):
        funcs.append(f(
                        x1(start, finish, N, i)
                      ))
    res = funcs[0] - funcs[2 * N] #вычитаем f[2N] т.к. цикл до N-1 по формуле 1.6

    for j in range(0, N + 1):
        res += 4 * funcs[2 * j - 1] + 2 * funcs[2 * j] # 2 * funcs[2j] потому что мы 2 раза считаем четный шаг

    return (finish - start) / (6 * N) * res #оценка сверху

print("Интегранд: sin(100x)*(e**-x**-2)*cos(2x)\n",
      "Пределы интегрирования: [0; 3]\n",
      "Шаг: 10000")

result = simpson(func, 0, 3, 10000)
print("Вычисление методом Симпсона дало следующее значение: ", round(result, 6), "      (точность 10**-6)")