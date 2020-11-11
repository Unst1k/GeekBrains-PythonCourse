months = {'1': 'Январь',
          '2': 'Февраль',
          '3': 'Март',
          '4': 'Апрель',
          '5': 'Май',
          '6': 'Июнь',
          '7': 'Июль',
          '8': 'Август',
          '9': 'Сентябрь',
          '10': 'Октябрь',
          '11': 'Ноябрь',
          '12': 'Декабрь'}
year_times = ['Зима', 'Весна', 'Лето', 'Осень']

user_month = input('Введите номер месяца (любое число от 1 до 12): ')

if int(user_month) <= 0 or int(user_month) > 12:
    print(f'Вы ввели некорректное число!')
elif int(user_month) <= 2 or int(user_month) == 12:
    print(f'Вы ввели число {user_month}, месяц {months.get(user_month)}, время года {year_times[0]}')
elif int(user_month) == 3 or int(user_month) < 6:
    print(f'Вы ввели число {user_month}, месяц {months.get(user_month)}, время года {year_times[1]}')
elif int(user_month) == 6 or int(user_month) < 9:
    print(f'Вы ввели число {user_month}, месяц {months.get(user_month)}, время года {year_times[2]}')
else:
    print(f'Вы ввели число {user_month}, месяц {months.get(user_month)}, время года {year_times[3]}')
