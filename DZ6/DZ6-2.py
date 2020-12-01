# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.

class Road:
    _road_length: int
    _road_width: int
    asphalt_mass = 25
    asphalt_thickness = 5

    def __init__(self, _road_length, _road_width):
        self._road_length = _road_length
        self._road_width = _road_width

    def total_result(self):
        result = round((self._road_length * self._road_width * self.asphalt_mass * self.asphalt_thickness) / 1000)
        print(f'\nРасчет массы асфальта, необходимого для покрытия всего дорожного полотна: '
              f'{self._road_length}м * {self._road_width}м * {self.asphalt_mass}кг * '
              f'{self.asphalt_thickness}см = {result} т')


first_measure = Road(20, 5000)
first_measure.total_result()

second_measure = Road(47, 14000)
second_measure.total_result()
