# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(user_name, user_surname, user_birth_year, user_city,
              user_email, user_tel):
    print(f'{user_name} {user_surname}, {user_birth_year} года рождения. Проживает в городе {user_city}.'
          f' Email пользователя: {user_email}. Телефон пользователя: {user_tel}.')


print('Введите данные и получите краткую информацию о себе!')
while True:
    try:
        name, surname = input('Введите Имя и Фамилию через пробел: ').split(' ')
        birth_year = int(input('Введите год рождения: '))
        city = input('Введите город проживания: ')
        email = input('Введите ваш email: ')
        tel = int(input('Введите номер телефона(без пробелов и спец. символов): '))

        user_data(user_name=name, user_surname=surname, user_birth_year=birth_year, user_city=city,
                  user_email=email, user_tel=tel)
        break
    except ValueError:
        print('Введено некорректное значение!')
