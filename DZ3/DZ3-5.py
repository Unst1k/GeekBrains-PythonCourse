# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

def numbers_sum(numbers_list):
    print(f'Сумма введенных чисел: {sum(numbers_list)}.')
    return sum(numbers_list)


a = 0
while True:
    try:
        user_numbers = input('Введите любое количество чисел через пробел. '
                             'Для выхода введите символ "@": ').split(' ')
        user_numbers_list = [a]
        if '@' in user_numbers:
            for i in user_numbers:
                if i.isdigit():
                    user_numbers_list.append(int(i))
                elif i == '@':
                    break
            numbers_sum(user_numbers_list)
            break
        else:
            for i in user_numbers:
                user_numbers_list.append(int(i))
            a = numbers_sum(user_numbers_list)
    except ValueError:
        print('Введено некорректное значение!')
