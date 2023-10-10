'''Задание №7
📌 Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
📌 Для цифры верните её квадрат, например 5 - 25
📌 Для двузначного числа произведение цифр, например 30 - 0
📌 Для трёхзначного числа его зеркальное отображение, например 520 - 25
📌 Если число не из диапазона, запросите новое число
📌 Откажитесь от магических чисел
📌 В коде должны быть один input и один print'''

while True:
    number = int(input('Введите число: '))
    if number < 1 or number > 999:
        print('Число не из диапозона 1-999')
        continue
    elif number < 10:
        print(number, '-', number ** 2)
    elif 9 < number < 100:
        print(number, '-', (number % 10) * (number // 10))
    elif number > 99:
        res = 0
        while number != 0:
            res = (res * 10) + (number % 10)
            number //= 10
        print(res)