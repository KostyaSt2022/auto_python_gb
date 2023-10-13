"""
Задание №5
Погружение в Python | Коллекции
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
"""

lst = [2, 2, 2, 3, 3, 5]

new_list = []

# for i in range(len(lst)):
#     if lst[i] % 2 == 1:
#         new_list.append(i + 1)
#
# print(new_list)

new_list = [i + 1 for i in range(len(lst)) if lst[i] % 2 == 1]
print(new_list)