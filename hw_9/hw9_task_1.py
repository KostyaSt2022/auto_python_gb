"""
Генерация случайных данных и нахождение корней квадратного уравнения.
Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке,
от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
Функция принимает три аргумента:

a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

Пример
На входе:
generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)

На выходе:
True
True
"""

import csv
import datetime
import json
import math
import os.path
from random import randint as RI
from typing import Callable


def generate_csv_file(func: Callable):
    create_csv_file()

    def wrapper():
        with open('coef_equation.csv', 'r', encoding='UTF-8') as file:
            data = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for coef in data:
                if coef and coef[0] != 0:
                    func(*coef)

    return wrapper


def json_result(func: Callable):
    result = {}
    if os.path.exists('solutions.json'):
        with open('solutions.json', 'r', encoding='UTF-8') as file:
            result = json.load(file)

    def wrapper(*args):
        roots = func(*args)
        solve_dict = {'a': args[0], 'b': args[1], 'c': args[2], 'roots': roots}
        res_key = f'{datetime.datetime.now()}'[:-7]
        result[res_key] = result.get(res_key) + [solve_dict] if result.get(res_key) else [solve_dict]
        with open('solutions.json', 'w', encoding='UTF-8') as file:
            json.dump(result, file)
        return roots

    return wrapper


def create_csv_file():
    with open('coef_equation.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in range(RI(100, 1000)):
            writer.writerow([RI(-100, 100), RI(-100, 100), RI(-100, 100)])


@generate_csv_file
@json_result
def solve_square_equation(*args) -> tuple | float | None:
    a, b, c = args
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        x1 = (-b + math.sqrt(disc)) / (2 * a)
        x2 = (-b - math.sqrt(disc)) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif disc == 0:
        x = -b / (2 * a)
        return round(x, 2)


solve_square_equation()



# Решение от ГБ:
#
# import csv
# import json
# import random
#
# def save_to_json(func):
#     def wrapper(*args):
#         result_list = []
#         with open(args[0], 'r') as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 a, b, c = map(int, row)
#                 result = func(a, b, c)
#                 data = {'parameters': [a, b, c], 'result': result}
#                 result_list.append(data)
#         with open('results.json', 'w') as f:
#             json.dump(result_list, f)
#     return wrapper
#
# @save_to_json
# def find_roots(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d < 0:
#         return None
#     elif d == 0:
#         return -b / (2 * a)
#     else:
#         x1 = (-b + d ** 0.5) / (2 * a)
#         x2 = (-b - d ** 0.5) / (2 * a)
#         return x1, x2
#
# def generate_csv_file(file_name, rows):
#     with open(file_name, 'w', newline='') as f:
#         writer = csv.writer(f)
#         for i in range(rows):
#             row = [random.randint(1, 1000) for _ in range(3)]
#             writer.writerow(row)