# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

numbers_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четрые'
}

new_list = []

with open('file_for_DZ5-4.txt', encoding='utf-8') as text:
    [new_list.append(f'{numbers_dict[i.split()[0]]} {i.split()[1]} {i.split()[2]}') for i in text]

with open('new_file.txt', 'w') as new_text:
    [print(i, file=new_text) for i in new_list]
