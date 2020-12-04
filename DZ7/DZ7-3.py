# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс
# Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()),
# вычитание (sub()), умножение (mul()), деление (truediv()). Данные методы должны применяться только к
# клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление
# клеток, соответственно.В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
# переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются
# все оставшиеся.

class Cell:
    cells_number: int

    def __init__(self, cells_number: int):
        self.cells_number = int(cells_number)

    def __add__(self, other):
        return Cell(self.cells_number + other.cells_number)

    def __sub__(self, other):
        return Cell(self.cells_number - other.cells_number)

    def __mul__(self, other):
        return Cell(self.cells_number * other.cells_number)

    def __truediv__(self, other):
        if other.cells_number == 0:
            return f'Нельзя делить на ноль!\n'
        else:
            return Cell(self.cells_number / other.cells_number)

    def __str__(self):
        return f'Количество клеток после проведенной операции: {self.cells_number * "*"} ({self.cells_number})'

    def make_rows(self, cells_in_row):
        row = 'Организация ячеек по рядам:\n'

        for i in range(round(int(self.cells_number) / cells_in_row)):
            row += f'{cells_in_row * "*"}\n'
        row += f'{(int(self.cells_number) % cells_in_row) * "*"}\n'
        return row


a = Cell(13)
b = Cell(6)
c = Cell(0)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a / c)

print(a.make_rows(5))
print(b.make_rows(5))
