# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def division_func(first_number, second_number):
    return round((first_number / second_number), 5)


while True:
    user_numbers = input('Введите через пробел два любых числа и система отобразит '
                         'результат их деления: ')
    try:
        if user_numbers == 'Exit':
            print('Вы вышли из программы!')
            break
        else:
            user_number1, user_number2 = user_numbers.split(' ')
            print(f'Результат деления: {division_func(int(user_number1), int(user_number2))}. '
                  f'Для выхода из программы введите слово "Exit"')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    except ValueError:
        print('Введно некорректное значение или не проставлен пробел!')
