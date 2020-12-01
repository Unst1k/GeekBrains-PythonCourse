# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и
# ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

salary_dict = {'Сергей Петров': {'wage': 30000, 'bonus': 7000},
               'Михаил Смирнов': {'wage': 10000, 'bonus': 5000}
               }


class Worker:
    name: str
    surname: str
    position: str
    _income = salary_dict

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        print(f'\nСотрудник: {self.name} {self.surname}\nДолжность: {self.position}')

    def get_total_income(self):
        if f"{self.name} {self.surname}" in self._income.keys():
            print(f'Доход с учетом премии: {sum(self._income[f"{self.name} {self.surname}"].values())} рублей.')
        else:
            print('Такого сотрудника нет!')


petrov = Position('Сергей', 'Петров', 'Менеджер')
petrov.get_full_name()
petrov.get_total_income()

smirnov = Position('Михаил', 'Смирнов', 'Грузчик')
smirnov.get_full_name()
smirnov.get_total_income()

tenev = Position('Михаил', 'Тенев', 'Иллюминат')
tenev.get_full_name()
tenev.get_total_income()
