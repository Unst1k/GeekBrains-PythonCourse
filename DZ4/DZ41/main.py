# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys
from DZ4.DZ41.salary_calc import salary_calc
'''
Параметры:
user_hours - выработка в часах;
user_rate - ставка в час;
user_bonus - премия
'''
try:
    file, user_hours, user_rate, user_bonus = sys.argv

    salary_calc(int(user_hours), int(user_rate), int(user_bonus))
except ValueError:
    print('\nДанные для расчета не указаны или указаны некорректно!')
