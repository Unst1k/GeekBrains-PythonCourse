# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования
# в исходном списке. Для выполнения задания обязательно использовать генератор.

from random import randint

numbers = [randint(1, 10) for i in range(1, 16)]
print(f'\nСписок случайных чисел с повторами от 1 до 15: {numbers}')

result_numbers = [i for i in numbers if numbers.count(i) == 1]
print(f'\nСписок чисел, у которых не было повторов: {result_numbers}')
