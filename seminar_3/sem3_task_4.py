"""
Задание №4
Погружение в Python | Коллекции
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""

lst = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5]
# dct = {}
# for item in lst:
#     dct[item] = dct.get(item, 0) + 1
#     # if lst.count(item) == 2:
# new_lst = [el for el in lst if dct[el] != 2]
# print(*new_lst)

#Решение №2
new_list = [item for item in lst if lst.count(item) != 2]
print(new_list)