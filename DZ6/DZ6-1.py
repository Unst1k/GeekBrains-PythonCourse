# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
# светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.
from time import sleep


class TrafficLight:
    _color = [['Красный', 7], ['Желтый', 2], ['Зеленый', 20]]

    def running(self):
        color_counter = 0

        while color_counter < 3:
            message = (f'На светофоре загорелся {TrafficLight._color[color_counter][0]} свет! '
                       f'Ждите {TrafficLight._color[color_counter][1]} секунд(ы)!')

            if color_counter == 0:
                print(message)
                sleep(7)
                color_counter += 1
            elif color_counter == 1:
                print(message)
                sleep(2)
                color_counter += 1
            else:
                print(f'На светофоре загорелся {TrafficLight._color[color_counter][0]} свет! '
                      f'Можно идти {TrafficLight._color[color_counter][1]} секунд(ы)!')
                sleep(20)
                color_counter += 1
                print('Светофор отработал корректно, выполнение программы остановлено!')
                break


light = TrafficLight()
light.running()
