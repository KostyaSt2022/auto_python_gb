"""
Преобразование ключей и значений словаря
Напишите функцию key_params, принимающую на вход только ключевые параметры и
возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
___Пример использования___:
На входе:
params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)

___На выходе___:
{1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}
"""
# Решение №1%:
# def key_params(**params):
#     result = {}
#     for key, value in params.items():
#         try:
#             result[value] = key
#         except:
#             result[str(value)] = key
#     return result
#
#
# print(key_params(name='Константин', age=24,
#                  has_work=True, commands=['KM', 'OSPP', 'DIT'],
#                  growth=1.72, nicks={'Kostya', '_2121'}))



# Решение №2 (от Гб):
def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, str, float, bool, tuple)):
            result[value] = key
        else:
            result[str(value)] = key
    return result