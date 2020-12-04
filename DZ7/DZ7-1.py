# # Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# # который должен принимать данные (список списков) для формирования матрицы.
# # Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# # Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# # Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix
# # (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    list_items: list

    def __init__(self, list_items: list):
        self.list_items = list_items

    def __add__(self, other):
        result = [[0, 0, 0, 0],
                  [0, 0, 0, 0]]

        for list_len in range(len(self.list_items)):
            for list_len2 in range(len(other.list_items[list_len])):
                result[list_len][list_len2] = self.list_items[list_len][list_len2] + \
                                              other.list_items[list_len][list_len2]

        total = str('\n'.join(['\t'.join([str(item) for item in my_list]) for my_list in result]))
        return f'Результат сложения двух матриц:\n{total}'

    def __str__(self):
        my_matrix = str('\n'.join(['\t'.join([str(item) for item in my_list]) for my_list in self.list_items]))

        return f'Матрица:\n{my_matrix}\n'


first_matrix = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
second_matrix = Matrix([[9, 10, 11, 12], [13, 14, 15, 16]])

print(first_matrix)
print(second_matrix)
print(first_matrix + second_matrix)
