import numpy as np
import matplotlib.pyplot as plt


# правая часть дифференциального уравнения
def f(x, y):
    return -2 * y / (x + 1)


# решение дифференциального уравнения, полученное при точном расчете
def solution(x):
    return np.e ** (1 / ((x + 1) ** 2))


# параметры, полученные из условия
a, b = 0, 1
x_first, y_first = 0, 1
n1, n2, n3 = 10, 20, 30


# реализация метода Эйлера явного
def euler_explicit(n):
    x_prev = x_first
    y_prev = y_first
    y_list = [y_prev]
    x_list = [x_prev]
    h = (b - a) / n
    for i in range(n):
        y_next = y_prev + h * f(x_prev, y_prev)
        y_prev = y_next
        x_prev += h
        y_list.append(y_next)
        x_list.append(x_prev)
    return y_next, y_list, x_list


# реализация метода Рунге_Кутта четвертого порядка
def runge_kutta(n):
    x_prev = x_first
    y_prev = y_first
    y_list = [y_prev]
    x_list = [x_prev]
    h = (b - a) / n
    for i in range(n):
        k1 = f(x_prev, y_prev)
        k2 = f(x_prev + h / 2, y_prev + h / 2 * k1)
        k3 = f(x_prev + h / 2, y_prev + h / 2 * k2)
        k4 = f(x_prev + h, y_prev + h * k3)
        y_next = y_prev + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y_prev = y_next
        x_prev += h
        y_list.append(y_next)
        x_list.append(x_prev)
    return y_next, y_list, x_list


# реализация метода Адамса-Бэшфорта трехшагового
def adams3(n):
    h = (b - a) / n
    x_prev2 = x_first
    y_prev2 = y_first
    y_prev1 = y_prev2 + h * f(x_prev2, y_prev2)
    x_prev1 = x_prev2 + h
    y_prev = y_prev1 + h / 2 * (3 * f(x_prev1, y_prev1) - (f(x_prev2, y_prev2)))
    x_prev = x_prev1 + h
    y_list = [y_prev2, y_prev1, y_prev]
    x_list = [x_prev2, x_prev1, x_prev]
    for i in range(2, n):
        y_next = y_prev + h / 12 * (23 * f(x_prev, y_prev) - 16 * f(x_prev1, y_prev1) + 5 * f(x_prev2, y_prev2))
        y_prev = y_next
        x_prev += h
        y_list.append(y_next)
        x_list.append(x_prev)
    return y_next, y_list, x_list


# функция, отвечающая за рисование графиков
def draw(x1, y1, x2, y2, x3, y3, title):
    plt.plot(x1, y1, 'g-', label='n = 10')
    plt.plot(x2, y2, 'b-', label='n = 20')
    plt.plot(x3, y3, 'r-', label='n = 30')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.show()


# функция, которая рисует решение solution при шаге 0.1
def draw_solution(x):
    x = np.arange(0, 1.01, 0.1)
    plt.plot(x, solution(x), label=r'y = e$^{(x+1)^{-2}}$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График решения уравнения')
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    y1, y_list_1, x_list_1 = euler_explicit(n1)
    y2, y_list_2, x_list_2 = euler_explicit(n2)
    y3, y_list_3, x_list_3 = euler_explicit(n3)
    draw(x_list_1, y_list_1, x_list_2, y_list_2, x_list_3, y_list_3, 'Метод Эйлера явный')

    y4, y_list_4, x_list_4 = runge_kutta(n1)
    y5, y_list_5, x_list_5 = runge_kutta(n2)
    y6, y_list_6, x_list_6 = runge_kutta(n3)
    draw(x_list_4, y_list_4, x_list_5, y_list_5, x_list_6, y_list_6, 'Метод Рунге-Кутта четвертого порядка')

    y7, y_list_7, x_list_7 = adams3(n1)
    y8, y_list_8, x_list_8 = adams3(n2)
    y9, y_list_9, x_list_9 = adams3(n3)
    draw(x_list_7, y_list_7, x_list_8, y_list_8, x_list_9, y_list_9, 'Метод Адамса трехшаговый явный')

    draw_solution(x_list_7)

