# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    # Сложение комплексных чисел: (a+b*i)+(c+d*i) = (a+c)+(b+d)*i
    def __add__(self, other):
        return f'Сумма комплексных чисел: z = {self.first_number + other.first_number} + ' \
               f'{self.second_number + other.second_number} * i\n'

    # Произведение комплексных чисел: (a+b*i)*(c+d*i) = (a*c - b*d) + (b*c + a*d) * i
    def __mul__(self, other):
        return f'Умножение комплексных чисел: ' \
               f'z = {((self.first_number * self.second_number) - (other.first_number * other.second_number))} ' \
               f'+ {((other.first_number * self.second_number) + (self.first_number * other.second_number))} * i'

    def __str__(self):
        return f'Комплексное число: z = {self.first_number} + {self.second_number} * i\n'


first_complex_number = ComplexNumber(11, -12)
second_complex_number = ComplexNumber(13, 14)

print(first_complex_number)

print(first_complex_number + second_complex_number)

print(first_complex_number * second_complex_number)
