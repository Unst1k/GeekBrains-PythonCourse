# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(first_number, second_number, third_number):
    numbers_list = [first_number, second_number, third_number]
    numbers_list.sort()
    print(f'Сумма двух наибольших цифр: {max(numbers_list) + numbers_list[1]}.')


while True:
    try:
        user_number1, user_number2, user_number3 = input('Введите три любых числа через пробел: ').split(' ')
        my_func(int(user_number1), int(user_number2), int(user_number3))
        break
    except ValueError:
        print('Введите три числа через пробел!')
