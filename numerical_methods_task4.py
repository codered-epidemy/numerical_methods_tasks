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


def formule_3_8_runge(h):
    r = (f(h) - f(h / 2)) / 3
    return abs(r)


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


def formule_trapezoid_runge(h):
    r = (1 / 3) * (f(h) - f(h / 2))
    return abs(r)


def gauss(a, b, c):
    return a*f((5-math.sqrt(15))/10)+b*f(1/2)+c*f((5+math.sqrt(15))/10)


def main():
    print('Формула 3/8:')

    res1 = formule_3_8(0, 1, h1)
    res2 = formule_3_8(0, 1, h2)
    res3 = formule_3_8(0, 1, h3)
    res_runge_3_8_1 = formule_3_8_runge(h1)
    res_runge_3_8_2 = formule_3_8_runge(h2)
    res_runge_3_8_3 = formule_3_8_runge(h3)
    print(f'Шаг: {h1}. Результат: {res1}', f'Шаг: {h2}. Результат: {res2}', f'Шаг: {h3}. Результат: {res3}', sep='\n',
          end='\n\n')
    print('Погрешность:', end='\n')
    print(f'Шаг: {h1}. Результат: {res_runge_3_8_1}', f'Шаг: {h2}. Результат: {res_runge_3_8_2}',
          f'Шаг: {h3}. Результат: {res_runge_3_8_3}', sep='\n')

    print('\n')

    res4 = formule_trapezoid(0, 1, h1)
    res5 = formule_trapezoid(0, 1, h2)
    res6 = formule_trapezoid(0, 1, h3)
    res_runge_trapezoid1 = formule_trapezoid_runge(h1)
    res_runge_trapezoid2 = formule_trapezoid_runge(h2)
    res_runge_trapezoid3 = formule_trapezoid_runge(h3)
    print('Формула трапеций:')
    print(f'Шаг: {h1}. Результат: {res4}', f'Шаг: {h2}. Результат: {res5}', f'Шаг: {h3}. Результат: {res6}', sep='\n',
          end='\n\n')
    print('Погрешность:', end='\n')
    print(f'Шаг: {h1}. Результат: {res_runge_trapezoid1}', f'Шаг: {h2}. Результат: {res_runge_trapezoid2}',
          f'Шаг: {h3}. Результат: {res_runge_trapezoid3}', sep='\n')

    print('\n')

    print(f'Расчет по формуле Гаусса с 3 узлами: {gauss(5/18, 4/9, 5/18)}')


if __name__ == '__main__':
    main()
