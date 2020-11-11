# Объявляю пустой список list_of_products для ввода информации о продуктах
list_of_products = []
# Объявляю переменную i и через цикл while даю пользователю возможнось ввести информацию о товарах
print('Введи информацию о трех продуктах, чтобы получить базовую аналитику.')

i = 0
while i != 3:
    name = input(f'Укажите название {i+1}-го товара: ')
    price = int(input(f'Укажите цену {i+1}-го товара (только цифры, без пробелов) (руб.): '))
    quantity = int(input(f'Укажите количество {i+1}-го товара (только цифры, без пробелов): '))
    measure = input(f'Укажите единицу измерения {i+1}-го товара: ')
    list_of_products.append((i+1, {'название': name, 'цена': price,
                                   'количество': quantity, 'eд': measure}))
    print(list_of_products[i])
    i += 1
print(f'\nОбщий список товаров:\n{list_of_products}\n')
# Создаю словарь analytics, где будет хранится аналитическая информация по товарам
analytics = {'название': [],
             'цена': [],
             'количество': [],
             'ед': []
             }
# Через цикл for in перебираю список продукции list_of_products забирая значения
# в соответствующие строки в словаре analytics
for a in list_of_products:
    analytics['название'].append(a[1]['название'])
    analytics['цена'].append(a[1]['цена'])
    analytics['количество'].append(a[1]['количество'])
    if a[1]['eд'] in analytics['ед']:
        continue
    else:
        analytics['ед'].append(a[1]['eд'])

print(f'Выборка товаров по параметрам:\n{analytics}')
