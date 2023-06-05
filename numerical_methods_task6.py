import matplotlib.pyplot as plt
import numpy as np
from numpy import exp

n = 10
h = 1 / n
p_x = 1
A = 2 + h ** 2
y = []
x_val = [0]


def analytic_solution(x):
    return exp(x) * exp(-x) + 2.7 * x ** 2 - 2.7 * x - 2


def q(x):
    return 7.4 + 2.7 * x * (1 - x)


def d(x):
    return q(x) * h ** 2


def progonka(h):
    l = [2 / (h ** 2 + 2 * h + 2)]
    mu = [(7.4 * h ** 2 - 5.4 * h) / (h ** 2 + 2 * h + 2)]

    for i in range(1, n + 1):
        x_val.append(x_val[-1] + h)
        l.append(1 / (A - l[i - 1]))
        mu.append((mu[i - 1] - d(x_val[i])) / (A - l[i - 1]))

    y.append(mu[-1])

    for i in range(n - 1, 0, -1):
        y.append(l[i + 1] * y[n - 1 - i] + mu[i + 1])

    y.reverse()

    roots = []

    for i in range(0, n + 1):
        roots.append(analytic_solution(x_val[i]))
    return roots


def draw_progonka(x, roots):
    plt.plot(x, roots, '-bo')
    plt.title(f'График прогонки. n = {n}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def draw_solution():
    x = np.arange(0, 1.01, 0.001)
    plt.plot(x, analytic_solution(x), '-g')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График точного решения')
    plt.grid(True)
    plt.show()


def main():
    roots = progonka(h)
    # print(roots)
    draw_solution()
    draw_progonka(x_val, roots)


if __name__ == '__main__':
    main()
