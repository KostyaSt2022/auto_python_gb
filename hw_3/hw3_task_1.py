"""
Список вещей для похода
На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
Достаточно получить один допустимый вариант и сохранить в переменную backpack. Напечатайте его.

*Пример*
На входе:
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

На выходе:
{'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}
"""


# def pack_backpack(items, max_weight):
#     possible_items = []
#     for item, weight in items.items():
#         if weight <= max_weight:
#             possible_items.append(item)
#             max_weight -= weight
#     return possible_items
#
#
# items = {'ключи': 0.3, 'кошелек': 0.2, 'телефон': 0.5, 'зажигалка': 0.1, 'ноутбук': 1.4, 'зарядное уст-во': 0.3}
# max_weight = 1.0
# print(pack_backpack(items, max_weight))


# Решение №2
items = {'ключи': 0.3, 'кошелек': 0.2, 'телефон': 0.5, 'зажигалка': 0.1, 'ноутбук': 1.4, 'зарядное уст-во': 0.3}
max_weight = 1.0
backpack = {}

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight