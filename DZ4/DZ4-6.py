from itertools import count, cycle


# Генерация целых чисел, начиная с указанного пользователем
def numbers_generator(user_number, the_last_number):
    for i in count(user_number):
        if i > the_last_number:
            break
        else:
            print(i)


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


def row_generator(user_row, repeat):
    row_count = 0
    for i in cycle(user_row):
        if row_count > (repeat*len(user_row)-1):
            break
        print(i)
        row_count += 1


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
