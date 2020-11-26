# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

# Функция считающая общее кол-во часов
def total_hours(any_list):
    hours = []
    for i in any_list:
        if '(л)' in i:
            hours.append(int(i.replace('(л)', '')))
        elif '(пр)' in i:
            hours.append(int(i.replace('(пр)', '')))
        elif '(лаб)' in i:
            hours.append(int(i.replace('(лаб)', '')))
        else:
            continue
    return sum(hours)


# Словарь с предметами и кол-во чаов по каждому
school_subjects = {}

with open('file_for_DZ5-6.txt', encoding='utf-8') as text:
    # Преобразовываю текстовый файл в лист с листами
    my_list = [line.split() for line in text]
    # Счетик, считающий кол-во предметов
    counter = 0
    while counter != len(my_list):
        school_subjects[my_list[counter][0].replace(':', '')] = total_hours(my_list[counter])
        counter += 1
    print(f'Общее количество занятий по предметам: {school_subjects}')
