from DZ4.DZ46.generators import numbers_generator, row_generator

# Генерация целых чисел, начиная с указанного пользователем

while True:
    try:
        any_number = input('Введите любое число с которого начнется последовательность. '
                           'Для перехода к следующей программе введите букву "E": ').lower()
        if any_number == 'e' or any_number == 'е':
            print('Вы перешли к следующей программе!')
            break
        last_number = input('Введите крайнее число, до которого будет идти последовательность: ')
        if last_number.isdigit() and int(last_number) > int(any_number):
            numbers_generator(int(any_number), int(last_number))
        else:
            print('Введено некорректное значение!')
    except ValueError:
        print('Введено некорректное значение!')

# Повтор элементов списка, указанного пользователем

while True:
    try:
        any_row = input('Введите любой набор символов без пробелов. '
                        'Для выхода из программы введите букву "E": ').lower()
        if ' ' in any_row:
            print('Введите строку без пробелов!')
            break
        elif any_row == 'e' or any_row == 'е':
            print('Вы вышли из программы!')
            break
        any_repeat = int(input('Введите количество повторов последовательности: '))
        row_generator(any_row, any_repeat)
    except ValueError:
        print('Введено некорректное значение!')
