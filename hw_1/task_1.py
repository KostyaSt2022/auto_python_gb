"""
Треугольник.
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.
Пример. На входе:
a = 4
b = 4
c = 4
На выходе:
1) Треугольник существует
Треугольник равносторонний

2) Треугольник существует
Треугольник равнобедренный

3) Треугольник существует
Треугольник разносторонний

4) Треугольник не существует
"""

# side_a = int(input('Введите длину стороны a: '))
# side_b = int(input('Введите длину стороны b: '))
# side_c = int(input('Введите длину стороны c: '))
#
# if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
#     print('Треугольник не существует.')
# elif side_a != side_b and side_a != side_c and side_b != side_c:
#     print(f'Треугольник существует.\nТреугольник разносторонний.')
# elif side_a == side_b == side_c:
#     print(f'Треугольник существует.\nТреугольник равносторонний')
# else:
#     print(f'Треугольник существует.\nТреугольник равнобедренный')

side_a = int(input('Введите длину стороны a: '))
side_b = int(input('Введите длину стороны b: '))
side_c = int(input('Введите длину стороны c: '))

if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
    print('\nТреугольник не существует')
elif (side_a != side_b) and (side_a != side_c) and (side_b != side_c):
    print(f'\nТреугольник существует\nТреугольник разносторонний')
elif side_a == side_b == side_c:
    print(f'\nТреугольник существует\nТреугольник равносторонний')
else:
    print(f'\nТреугольник существует\nТреугольник равнобедренный')

# # Эталонное решение от GB:
# if a + b > c and a + c > b and b + c > a:
#     print("Треугольник существует")
#     if a == b == c:
#         print("Треугольник равносторонний")
#     elif a == b or a == c or b == c:
#         print("Треугольник равнобедренный")
#     else:
#         print("Треугольник разносторонний")
# else:
#     print("Треугольник не существует")