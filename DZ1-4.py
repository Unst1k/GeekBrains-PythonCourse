user_number = int(input('Введите целое положительное число: '))
digits = []

for x in str(user_number):
    digits.append(int(x))

print(f'Самая большая цифра в числе {user_number} - это цифра {max(digits)}')
