km_first_day = int(input('Укажите количество километров, которые вы пробежали в первый день: '))
km_special_day = int(input('Укажите желаемое количество километров, которое вы хотите пробегать за день: '))
total_days = 0

while km_first_day < km_special_day:
    km_first_day = km_first_day + (km_first_day * 10) / 100
    total_days += 1

print(f'Если вы будете увеличивать нагрузку на 10% каждый день, то сможете пробегать '
      f'{km_special_day} километра(ов) через {total_days} дня(ей).')
