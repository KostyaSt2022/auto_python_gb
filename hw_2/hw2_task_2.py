"""
Действия с дробями
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей.
Для проверки своего кода используйте модуль fractions.
Пример
На входе:
frac1 = "1/2"
frac2 = "1/3"
На выходе:
Сумма дробей: 5/6
Произведение дробей: 1/6
Сумма дробей: 5/6
Произведение дробей: 1/6
"""

# from fractions import Fraction
#
# class SelfFraction:
#     def __init__(self, numerator: int, denominator: int):
#         if not isinstance(numerator, int) and not isinstance(denominator, int):
#             raise ValueError
#         elif denominator == 0:
#             raise ZeroDivisionError
#         else:
#             nod = SelfFraction.check_nod(numerator, denominator)
#             self.num = numerator // nod
#             self.den = denominator // nod
#
#     def __add__(self, other):
#         main_den = self.den * other.den
#         main_num = self.num * other.den + other.num * self.den
#         return SelfFraction(main_num, main_den)
#
#     def __mul__(self, other):
#         main_num = self.num * other.num
#         main_den = self.den * other.den
#         return SelfFraction(main_num, main_den)
#
#     @staticmethod
#     def check_nod(num: int, den: int) -> int:
#         nod = 1
#         for i in range(1, max(num, den) // 2 + 1):
#             if num % i == 0 and den % i == 0:
#                 nod = i
#         return nod
#
#     def __str__(self):
#         return f'{self.num}/{self.den}'
#
#
# frac1 = input('Введите первую дробь формата "a/b": ').split('/')
# frac2 = input('Введите вторую дробь формата "a/b": ').split('/')
#
# self_fract_1 = SelfFraction(int(frac1[0]), int(frac1[1]))
# self_fract_2 = SelfFraction(int(frac2[0]), int(frac2[1]))
# original_fract_1 = Fraction(int(frac1[0]), int(frac1[1]))
# original_fract_2 = Fraction(int(frac2[0]), int(frac2[1]))
#
# print(f'Сумма дробей: {self_fract_1 + self_fract_2}')
# print(f'Произведение дробей: {self_fract_1 * self_fract_2}')
#
# print(f'Сумма дробей: {original_fract_1 + original_fract_2}')
# print(f'Произведение дробей: {original_fract_1 * original_fract_2}')




# # Решение № 2
# from fractions import Fraction
# def process_fractions(frac1, frac2):
#     # Преобразуем дроби из строк в числа
#     num1, denom1 = map(int, frac1.split("/"))
#     num2, denom2 = map(int, frac2.split("/"))
#
#     # Вычисляем сумму дробей
#     sum_frac_num = num1 * denom2 + num2 * denom1
#     sum_frac_denom = denom1 * denom2
#     sum_frac = (sum_frac_num, sum_frac_denom)
#
#     # Вычисляем произведение дробей
#     prod_frac_num = num1 * num2
#     prod_frac_denom = denom1 * denom2
#     prod_frac = (prod_frac_num, prod_frac_denom)
#
#     # Проверка с помощью модуля
#     frac1_mod = Fraction(num1, denom1)
#     frac2_mod = Fraction(num2, denom2)
#     frac_sum_mod = frac1_mod + frac2_mod
#     frac_prod_mod = frac1_mod * frac2_mod
#
#     return sum_frac, prod_frac
#
# # Пример использования функции
# frac1 = "1/2"
# frac2 = "1/3"
#
# sum_frac, prod_frac = process_fractions(frac1, frac2)
#
# frac_sum_mod, frac_prod_mod = process_fractions(frac1, frac2)
#
# print(f"Сумма дробей: {sum_frac[0]}/{sum_frac[1]}")
# print(f"Произведение дробей: {prod_frac[0]}/{prod_frac[1]}")
#
# print(f"Сумма дробей: {frac_sum_mod[0]}/{frac_sum_mod[1]}")
# print(f"Произведение дробей: {frac_prod_mod[0]}/{frac_prod_mod[1]}")




# Эталон:
import fractions

frac1 = "1/2"
frac2 = "1/3"

numerator_1 = int(frac1.split('/')[0])
denominator_1 = int(frac1.split('/')[1])
numerator_2 = int(frac2.split('/')[0])
denominator_2 = int(frac2.split('/')[1])
nod = denominator_1 * denominator_2
print(f'Сумма дробей: {int(numerator_1 * (nod / denominator_1) + numerator_2 * (nod / denominator_2))}/{nod}')
print(f'Произведение дробей: {int(numerator_1 * numerator_2)}/{int(denominator_1 * denominator_2)}')
print(f'Сумма дробей: {fractions.Fraction(frac1) + fractions.Fraction(frac2)}')
print(f'Произведение дробей: {fractions.Fraction(frac1) * fractions.Fraction(frac2)}')


