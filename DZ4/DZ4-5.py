# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
from functools import reduce


def total_number(current_number, next_number):
    return current_number + next_number


numbers = [i for i in range(100, 1001) if i % 2 == 0]

total = reduce(total_number, numbers)

print(f'\nСумма всех четных чисел от 100 до 1000 - {total}.')
