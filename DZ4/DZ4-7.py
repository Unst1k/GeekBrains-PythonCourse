# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
<<<<<<< HEAD:DZ4/DZ4-7.py


def fact_number(number):
    for any_number in range(1, number + 1):
        yield any_number


def total_number(number):
    factorial = 1
    numbers_list = []
    for i in number:
        numbers_list.append(i)
        factorial *= i
    print(f'!{numbers_list[-1]} = {" * ".join(str(i) for i in numbers_list)} = {factorial}.')

=======
from factorial import total_number, fact_number
>>>>>>> f77855b5b50b23f95317e7da67199c65099594ac:DZ4/DZ47/main.py

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
