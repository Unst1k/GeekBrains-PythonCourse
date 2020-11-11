user_input = input('Введите несколько слов через пробел: ').split(' ')
string_number = 1

for i in user_input:
    print(f'{string_number} {i[:10]}')
    string_number += 1
