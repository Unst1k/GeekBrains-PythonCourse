# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('file_for_DZ5-3.txt', encoding='utf-8') as text:
    # user_list - в список из цикла for записываются зарплаты всех сотрудников
    # employee_number - считает из цикла for общее количество сотрудников
    # less_twenty - нумерует список работников с з.п. менее 20к
    users_list = []
    employee_number = 0
    less_twenty = 0
    print('\nСписок работников, которые получают меньше 20000 рублей:')
    for i in text:
        users_list.append(float(i.split()[1]))
        employee_number += 1
        if float(i.split()[1]) < 20000:
            less_twenty += 1
            print(f'{less_twenty}) {i.split()[0]}, {i.split()[1]} рублей')

    print(f'\nСредняя величина дохода сотрудников составляет: {round((sum(users_list) / employee_number), 2)} рублей.')
