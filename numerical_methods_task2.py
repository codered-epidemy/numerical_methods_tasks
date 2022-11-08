import math
from math import log

epsilon = 0.5e-5
segment = (1, 2)


def func(x=math.e):
    return log(x) - (0.15 / x)


def func_x(x=2):
    return math.e**(0.15/x)


def func_first_derivative(x=1):
    return 1 / x + 0.15 / x ** 2


def func_second_derivative(x=1):
    return -1 / x ** 2 - 0.3 / x ** 3


# find segment where the root is
# def find_segment():
#     b = 10
#     a = 9
#     while func(a) * func(b) >= 0:
#         b = a
#         a -= 1
#     return a, b


def method_of_half_division(epsilon, segment):
    n = 0
    a, b = segment
    x = abs(a + b) / 2
    while abs(segment[1] - segment[0]) >= epsilon:
        x = abs(segment[0] + segment[1]) / 2
        if func(x) * func(a) < 0:
            segment = segment[0], x
            method_of_half_division(epsilon, segment)
        elif func(x) * func(b) < 0:
            segment = x, segment[1]
            method_of_half_division(epsilon, segment)
        n += 1
    return x, n


def find_x0(segment):
    if func(segment[1]) * func_second_derivative(segment[1]) > 0:
        return segment[1]
    elif func(segment[0]) * func_second_derivative(segment[0]) > 0:
        return segment[0]


def method_newton(epsilon):
    n = 0
    first_x = find_x0(segment)
    x = first_x - func(first_x) / func_first_derivative(first_x)
    while abs(x - first_x) >= epsilon:
        first_x = x
        x = x - func(x) / func_first_derivative(x)
        n += 1
    return x, n


def method_newton_modified(epsilon):
    n = 0
    first_x = find_x0(segment)
    x1 = first_x
    x = first_x - func(first_x) / func_first_derivative(first_x)
    while abs(x - x1) >= epsilon:
        x1 = x
        x = x - func(x) / func_first_derivative(first_x)
        n += 1
    return x, n


def method_chord(epsilon, segment=(1, 2)):
    n = 0
    a, x_prev = segment
    # first_x = find_x0(segment)
    x_curr = a - (func(a) * (x_prev - a)) / (func(x_prev) - func(a))
    while abs(x_curr - x_prev) >= epsilon:
        x_prev = x_curr
        x_curr = a - (func(a) * (x_prev - a)) / (func(x_prev) - func(a))
        n += 1
    return x_curr, n


def method_chord_moving(epsilon):
    n = 0
    a, b = segment
    x_curr = b - (func(b) * (b-a)) / (func(b)-func(a))
    while abs(b-a) >= epsilon:
        a = b
        b = x_curr
        x_curr = b - (func(b) * (b-a)) / (func(b)-func(a))
        n += 1
    return x_curr, n


def method_simple_iteration(epsilon):
    n = 0
    x_prev = 1
    x_curr = func_x(x_prev)
    while abs(x_curr - x_prev) >= epsilon:
        x_prev = x_curr
        x_curr = func_x(x_prev)
        n += 1
    return x_curr, n


def main():
    # segment = find_segment()
    # print(segment[0], func(segment[0]))
    # print(segment[1], func(segment[1]))

    print("Метод половинного деления отрезка")
    x_half_division, n_half_division = method_of_half_division(epsilon, segment)
    print(x_half_division, n_half_division, sep='\n')
    print()

    print("Метод Ньютона")
    x_newton, n_newton = method_newton(epsilon)
    print(x_newton, n_newton, sep='\n')
    print()

    print("Метод Ньютона модифицированный")
    x_newton_modified, n_newton_modified = method_newton_modified(epsilon)
    print(x_newton_modified, n_newton_modified, sep='\n')
    print()

    print("Метод неподвижных хорд")
    x_chord, n_chord = method_chord(epsilon)
    print(x_chord, n_chord, sep='\n')
    print()

    print("Метод подвижных хорд")
    x_chord_moving, n_chord_moving = method_chord_moving(epsilon)
    print(x_chord_moving, n_chord_moving, sep='\n')
    print()

    print("Метод простой итерации")
    x_simple_iter, n_simple_iter = method_simple_iteration(epsilon)
    print(x_simple_iter, n_simple_iter, sep='\n')
    print()


if __name__ == '__main__':
    main()
