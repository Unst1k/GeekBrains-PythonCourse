# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
from factorial import total_number, fact_number

while True:
    user_number = input('Введите число, чтобы вычислить его факториал: ').lower()
    if user_number.isdigit():
        total_number(fact_number(int(user_number)))
        print('Для выхода из программы введите "E"')
    elif user_number == 'e' or user_number == 'е':
        print('Вы вышли из программы!')
        break
    else:
        print('Введено некорректное значение!')
