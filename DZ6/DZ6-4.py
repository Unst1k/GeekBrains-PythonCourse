# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed: int or float
    color: str
    name: str
    is_police: True or False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'\nТранспортное средство "{self.name}" {self.color} цвета начало движение.')

    def stop(self):
        print(f'\nТранспортное средство "{self.name}" {self.color} цвета остановилось.')

    def turn_right(self):
        print(f'\nТранспортное средство "{self.name}" {self.color} цвета повернуло направо.')

    def turn_left(self):
        print(f'\nТранспортное средство "{self.name}" {self.color} цвета повернуло налево.')

    def show_speed(self):
        print(f'\nТекущая скорость транспортного средства "{self.name}" {self.color} цвета '
              f'составляет {self.speed} км/ч.')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'\nТекущая скорость транспортного средства "{self.name}" {self.color} составляет '
                  f'{self.speed} км/ч. ТС превышает скорость на {self.speed - 60} км/ч!')
        else:
            print(f'\nТекущая скорость транспортного средства "{self.name}" {self.color} составляет '
                  f'{self.speed} км/ч. ТС едет в пределах разрешенной скорости!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'\nТекущая скорость транспортного средства "{self.name}" {self.color} составляет '
                  f'{self.speed} км/ч. ТС превышает скорость на {self.speed - 40} км/ч!')
        else:
            print(f'\nТекущая скорость транспортного средства "{self.name}" {self.color} составляет '
                  f'{self.speed} км/ч. ТС едет в пределах разрешенной скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        print(f'\nТранспортное средство марки "{self.name}" {self.color} цвета является полицейской машиной.')


Toyota = TownCar(70, 'белого', 'Toyota', False)
Toyota.go()
Toyota.show_speed()

Mitsubishi = SportCar(100, 'красного', 'Mitsubishi', False)
Mitsubishi.turn_right()
Mitsubishi.stop()

CAT = WorkCar(40, 'оранжевого', 'CAT', False)
CAT.turn_left()
CAT.show_speed()

Lada = PoliceCar(90, 'бело-синего', 'Lada', True)
Lada.police()
Lada.show_speed()
