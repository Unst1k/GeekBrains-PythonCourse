# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие
# только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и
# заполнять список только числами. Класс-исключение должен контролировать типы данных элементов списка.

class NotNumberException(Exception):
    def __init__(self, txt):
        self.txt = txt


user_list = []
numbers_counter = 1

print('\nWelcome to the program, which collects numbers into a list of numbers.\nPlease input only one number'
      ' at a time.\nFor exit press "Enter"!')

while True:
    try:
        user_number = input(f'\nInput {numbers_counter} number: ')

        if user_number == '':
            print('\nSuccessful exit!')
            break

        elif not user_number.isdigit():
            raise NotNumberException('Not a number')

        else:
            user_list.append(int(user_number))
            numbers_counter += 1

    except NotNumberException:
        print('Please input only numbers or only one number at a time!')

if not user_list:
    print('List of numbers is empty :(')

else:
    print(f'Your list of numbers: {", ".join([str(number) for number in user_list])}')
