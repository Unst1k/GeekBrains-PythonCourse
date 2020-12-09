# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его
# работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivisionException(Exception):
    def __init__(self, txt):
        self.txt = txt


exit_phrase = 'Press "Enter" to exit.\n'

while True:
    try:
        user_numbers = input('Input two numbers separated by space: ')
        split_numbers = user_numbers.split(' ')

        if user_numbers == '':
            print('Successful exit')
            break

        elif len(split_numbers) >= 3:
            print('You need to input only two numbers separated by space!')

        else:
            if int(split_numbers[1]) == 0:
                raise ZeroDivisionException("You can't divide by zero!")

            else:
                print(f'Result of division {split_numbers[0]} and {split_numbers[1]}: '
                      f'{round((int(split_numbers[0]) / int(split_numbers[1])), 2)}')
                print(exit_phrase)

    except ValueError:
        print('Incorrect input! Please input two numbers separated by space.')
        print(exit_phrase)

    except ZeroDivisionException:
        print("You can't divide by zero!")
        print(exit_phrase)

    except IndexError:
        print('Incorrect input! Please input two numbers separated by space.')
