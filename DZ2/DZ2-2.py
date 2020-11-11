user_list = input('Введите любое количество значений через запятую: ').split(",")
print(f'Ваш список {user_list}')

i = 0
while True:
    if i < len(user_list) - 1:
        user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
        i += 2
    else:
        print(f'Итоговый список {user_list}')
        break
