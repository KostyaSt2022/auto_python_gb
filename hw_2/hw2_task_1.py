"""
Шестнадцатеричное представление
Напишите программу, которая получает целое число num
и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
Пример
На входе:
num = 255
На выходе:
Шестнадцатеричное представление числа: FF
Проверка результата: 0xff
"""

num = int(input('Введите число в десятичной системе: '))

def self_hex(number: int) -> str:
    if not number:
        return '0x0'
    result = ''
    hex_letters = list('0123456789abcdef')
    while number > 0:
        result = hex_letters[number % 16] + result
        number //= 16
    return result

print(f'Шестнадцатеричное представление числа: {self_hex(num).upper()}')
print(f'Проверка результата: {hex(num)}')


# # Эталонное решение от GB:
# HEX = 16
# hex_digits = "0123456789ABCDEF"
#
# hex_num = ""
# test_hex_num = hex(num)
#
# while num > 0:
#     remainder = num % HEX
#     hex_num = hex_digits[remainder] + hex_num
#     num //= HEX
#
# print("Шестнадцатеричное представление числа:", hex_num)
# print("Проверка результата:", test_hex_num)