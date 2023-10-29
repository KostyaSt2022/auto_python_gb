"""
Транспонирование матрицы
Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix,
и возвращает транспонированную матрицу.
___Пример использования На входе___:
matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
transposed_matrix = transpose(matrix)

___На выходе___:
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""
# Решение №1:
# def transpose(matrix):
#     return [list(x) for x in zip(*maxrix)]
#
#
# maxrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# print(transpose(maxrix))


# Решение №2 (идеал от Гб):
def transpose(matrix):
    # определяем количество строк и столбцов в матрице
    rows = len(matrix)
    cols = len(matrix[0])

    # создаем новую матрицу с размерами, поменянными местами
    transposed = [[0 for row in range(rows)] for col in range(cols)]

    # заполняем новую матрицу значениями из старой матрицы
    for row in range(rows):
        for col in range(cols):
            transposed[col][row] = matrix[row][col]

    return transposed