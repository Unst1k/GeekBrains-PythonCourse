# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

try:
    # Сразу преобразовываю в список int чтобы исключить все, кроме цифр
    numbers_list = list(map(int, input('Введите любое количество чисел через пробел: ').split()))
    # Записываю в новый файл набор цифр введенных пользователем
    with open('some_numbers.txt', 'w') as numbers:
        numbers.writelines(' '.join([str(number) for number in numbers_list]))
    # Преобразовываю строку в списке в список и считаю сумму чисел в файле, вывожу на экран
    with open('some_numbers.txt') as numbers_sum:
        my_numbers = [int(i) for i in [line.split() for line in numbers_sum][0]]
        print(f'Сумма введенных чисел: {sum(my_numbers)}.')
except ValueError:
    print('Введено некорректное значение!')
