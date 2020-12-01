# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
# title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение. Создать
# экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('\nЗапуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'\nВы выбрали инструмент "{self.title}". Инициализация отрисовки.')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'\nИнструмент "{self.title}" в настоящее время недоступен для использования.')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'\nИнструмент "{self.title}" доступен для выбора только пользователям с правами администратора!')


my_stationery = Stationery('Канцелярская принадлежность')
my_stationery.draw()

my_pen = Pen('Ручка')
my_pen.draw()

my_pencil = Pencil('Карандаш')
my_pencil.draw()

my_handle = Handle('Маркер')
my_handle.draw()
