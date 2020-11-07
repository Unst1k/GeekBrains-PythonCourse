total_money = int(input('Введите значение выручки (руб.): '))
total_loss = int(input('Введите значение издержки (руб.): '))
net_profit = total_money - total_loss

if total_money >= total_loss:
    print(f'Вы работаете с прибылью! Рентабельность выручки '
          f'составляет {round((net_profit / total_money) * 100)}%.')
else:
    print('Вы работает в убыток =(')

total_employees = int(input('Укажите количество сотрудников в вашей компании: '))
print(f'Прибыль в фирме в расчете на сотрудника составляет {round(net_profit / total_employees)}'
      f' рублей на одного сотрудника.')
