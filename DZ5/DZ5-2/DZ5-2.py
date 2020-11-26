# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('file_for_DZ5-2.txt') as text:
    str_number = 0
    for i in text:
        str_number += 1
        print(f'Количество слов в {str_number}-ой строке: {len(i.split())}')
    print(f'Количество строк в файле: {str_number}.')
