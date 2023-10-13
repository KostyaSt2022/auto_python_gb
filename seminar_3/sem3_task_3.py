"""
Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где:
ключ - тип элемента,
значение - список элементов данного типа.
"""
# Решение № 1
tuple_obj = (1, 2.1, True, None, 'string', 3, 4, 5, False, 'elem')
dct = {}
for item in tuple_obj:
    obj_type = type(item)
    lst = []
    for elem in tuple_obj:
        if type(elem) == obj_type:
            lst.append(elem)
    dct[obj_type] = lst
print(dct)


# Решение № 2
# data = (1, 2.1, True, None, 'string', 3, 4, 5, False, 'elem')
#
# result_dict = dict()
#
# for el in data:
#     el_type = str(type(el))
#     if el_type not in result_dict.keys():
#         result_dict[el_type] = [el]
#     else:
#         result_dict[el_type].append(el)
# print(result_dict)