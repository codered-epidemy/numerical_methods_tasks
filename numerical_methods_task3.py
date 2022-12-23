from __future__ import annotations

import copy
import math
from collections.abc import Sequence, MutableSequence

import numpy as np

epsilon = 5e-5

matrix_full = [[1.40, 1.59, -0.13, 5.53],
               [0.14, -0.70, 0.93, 1.58],
               [-0.50, -0.25, -0.23, -2.21]]

matrix_left = [[1.40, 1.59, -0.13],
               [0.14, -0.70, 0.93],
               [-0.50, -0.25, -0.23]]

matrix_right = [5.53,
                1.58,
                -2.21]

matrix_modified_left = [[-0.50, -0.25, -0.23],
                        [1.40, 1.59, -0.13],
                        [0.14, -0.70, 0.93]]

matrix_modified_right = [-2.21,
                         5.53,
                         1.58]


def gauss_method(matrix):
    n = len(matrix)
    cloned_matrix = copy.deepcopy(matrix)

    for k in range(n):
        for i in range(n + 1):
            cloned_matrix[k][i] = cloned_matrix[k][i] / matrix[k][k]
        for i in range(k + 1, n):
            factor = cloned_matrix[i][k] / cloned_matrix[k][k]
            for j in range(n + 1):
                cloned_matrix[i][j] = cloned_matrix[i][j] - cloned_matrix[k][j] * factor
        for i in range(n):
            for j in range(n + 1):
                matrix[i][j] = cloned_matrix[i][j]

    for k in range(n - 1, -1, -1):
        for i in range(n, -1, -1):
            cloned_matrix[k][i] = cloned_matrix[k][i] / matrix[k][k]
        for i in range(k - 1, -1, -1):
            factor = cloned_matrix[i][k] / cloned_matrix[k][k]
            for j in range(n, -1, -1):
                cloned_matrix[i][j] = cloned_matrix[i][j] - cloned_matrix[k][j] * factor

    result = []
    for i in range(n):
        result.append(cloned_matrix[i][n])
    return result


def find_max_row(matrix, col):
    max_element = matrix[col][col]
    max_row = col
    for i in range(col + 1, len(matrix)):
        if abs(matrix[i][col]) > abs(max_element):
            max_element = matrix[i][col]
            max_row = i
    if max_row != col:
        matrix[col], matrix[max_row] = matrix[max_row], matrix[col]


def gauss_method_modified(matrix):
    n = len(matrix)
    for k in range(n - 1):
        find_max_row(matrix, k)
        for i in range(k + 1, n):
            div = matrix[i][k] / matrix[k][k]
            matrix[i][-1] -= div * matrix[k][-1]
            for j in range(k, n):
                matrix[i][j] -= div * matrix[k][j]

    result = [0 for i in range(n)]
    for k in range(n - 1, -1, -1):
        result[k] = (matrix[k][-1] - sum([matrix[k][j] * result[j] for j in range(k + 1, n)])) / matrix[k][k]
    return result


def isNeedToComplete(x_old, x_new):
    sum_up = 0
    sum_low = 0
    for k in range(0, len(x_old)):
        sum_up += (x_new[k] - x_old[k]) ** 2
        sum_low += (x_new[k]) ** 2

    return math.sqrt(sum_up / sum_low) < epsilon


def jacobi_method(matrix_left, matrix_right):
    amount_of_X = len(matrix_right)

    x = [1 for k in range(0, amount_of_X)]

    numberOfIter = 0  # подсчет количества итераций
    while numberOfIter < 100:

        x_prev = copy.deepcopy(x)

        for k in range(0, amount_of_X):
            S = 0
            for j in range(0, amount_of_X):
                if j != k:
                    S = S + matrix_left[k][j] * x[j]
            x[k] = matrix_right[k] / matrix_left[k][k] - S / matrix_left[k][k]

        if isNeedToComplete(x_prev, x):
            break

        numberOfIter += 1

    return x, numberOfIter


def gauss_seidel_method(matrix_left, matrix_right, eps):
    n = len(matrix_left)
    x = np.zeros(n)
    i = 0

    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(matrix_left[i][j] * x_new[j] for j in range(i))
            s2 = sum(matrix_left[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (matrix_right[i] - s1 - s2) / matrix_left[i][i]

        converge = np.linalg.norm(x_new - x) <= eps
        x = x_new
        i += 1

    return x, i


def main():
    print('Метод Гаусса:')
    print(gauss_method(matrix_full)[0],
          gauss_method(matrix_full)[1],
          gauss_method(matrix_full)[2], sep='\n')
    print('_____________________________________________________________')
    print('Метод Гаусса с выбором главного элемента по всей матрице:')
    print(gauss_method_modified(matrix_full)[0],
          gauss_method_modified(matrix_full)[1],
          gauss_method_modified(matrix_full)[2], sep='\n')
    print('_____________________________________________________________')
    print('Метод Якоби:')
    print(f'Количество итераций: {jacobi_method(matrix_modified_left, matrix_modified_right)[1]}')
    print(jacobi_method(matrix_modified_left, matrix_modified_right)[0][0],
          jacobi_method(matrix_modified_left, matrix_modified_right)[0][1],
          jacobi_method(matrix_modified_left, matrix_modified_right)[0][2],
          sep='\n')
    print('_____________________________________________________________')
    print('Метод Гаусса-Зейделя')
    print(f'Количество итераций: {gauss_seidel_method(matrix_modified_left, matrix_modified_right, epsilon)[1]}')
    print(gauss_seidel_method(matrix_modified_left, matrix_modified_right, epsilon)[0][0],
          gauss_seidel_method(matrix_modified_left, matrix_modified_right, epsilon)[0][1],
          gauss_seidel_method(matrix_modified_left, matrix_modified_right, epsilon)[0][2],
          sep='\n')
    print('_____________________________________________________________')


if __name__ == '__main__':
    main()
