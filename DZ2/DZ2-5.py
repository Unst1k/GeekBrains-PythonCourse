my_list = [7, 5, 3, 3, 2]
print('Добро пожаловать в "Рейтинг". Каждое введенное вами число будет располагаться '
      'в списке в соответствие с его величиной.\nДля выхода из игры введите любую букву.')
while True:
    try:
        user_number = int(input('Введите любое натуральное целое число: '))
        for i in my_list:
            if user_number < my_list[len(my_list)-1]:
                my_list.append(user_number)
                print(my_list)
                break
            elif user_number >= i:
                my_list[my_list.index(i):my_list.index(i)] = [user_number]
                print(my_list)
                break
    except ValueError:
        print('Вы вышли из программы!')
