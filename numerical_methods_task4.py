import math


def f(x):
    return math.cos(math.e ** (x / 3) + x)


a, b = 0, 1
h1, h2, h3 = 0.1, 0.05, 0.025


def formule_3_8(a, b, h):
    x_prev = a
    x_curr = x_prev
    res_3_8 = 0
    iter_count = (b - a) / h
    n = 0
    while n - 1 != iter_count:
        n += 1
        res_3_8 += (f(x_prev) + 3 * f((2 * x_prev + x_curr) / 3) + 3 * f((x_prev + 2 * x_curr) / 3) + f(x_curr)) / 8 * (x_curr - x_prev)
        x_prev = x_curr
        x_curr += h
    return res_3_8


def formule_trapezoid(a, b, h):
    x_prev = a
    x_curr = x_prev
    res_trapezoid = 0
    iter_count = (b - a) / h
    n = 0
    while n - 1 != iter_count:
        n += 1
        res_trapezoid += (f(x_prev) + f(x_curr)) / 2 * (x_curr - x_prev)
        x_prev = x_curr
        x_curr += h
    return res_trapezoid


def main():
    print('Формула 3/8:')

    res1 = formule_3_8(0, 1, h1)
    res2 = formule_3_8(0, 1, h2)
    res3 = formule_3_8(0, 1, h3)
    print(f'Шаг: {h1}. Результат: {res1}', f'Шаг: {h2}. Результат: {res2}', f'Шаг: {h3}. Результат: {res3}', sep='\n')
    print('\n')
    res4 = formule_trapezoid(0, 1, h1)
    res5 = formule_trapezoid(0, 1, h2)
    res6 = formule_trapezoid(0, 1, h3)
    print('Формула трапеций:')

    print(f'Шаг: {h1}. Результат: {res4}', f'Шаг: {h2}. Результат: {res5}', f'Шаг: {h3}. Результат: {res6}', sep='\n')


if __name__=='__main__':
    main()
