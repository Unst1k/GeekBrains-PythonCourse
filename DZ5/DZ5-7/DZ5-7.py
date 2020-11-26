# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
import json


def short_info(info_list):
    dicts_list = []
    companies_profit_dict = {}
    companies_loss_dict = {}
    average_profit_dict = {}
    order_counter = 0
    company_counter = 0
    total_profit = 0
    # dicts_list - лист со словарями companies_profit_dict, companies_loss_dict, average_profit_dict
    # companies_profit_dict - словарь с компаниями, которые приносят прибыль
    # companies_loss_dict - словарь с компаниями, которые работают в убыток
    # average_profit_dict - словарь со средней прибылью по компаниям
    # order_counter - счетчик для вывода нумерованого списка компаний
    # company_counter - счетчик количества компаний, которые приносят прибыль
    # total_profit - общая прибыль
    print('\nКраткая справка по компаниям:')
    for i in info_list:
        if (int(i[2]) - int(i[3])) > 0:
            order_counter += 1
            company_counter += 1
            companies_profit_dict[i[0]] = (int(i[2]) - int(i[3]))
            print(f'{order_counter}) Прибыль компании "{i[0]}" составляет: {(int(i[2]) - int(i[3]))} рублей.')
            total_profit += (int(i[2]) - int(i[3]))
        else:
            order_counter += 1
            companies_loss_dict[i[0]] = (int(i[2]) - int(i[3]))
            print(f'{order_counter}) Компания "{i[0]}" работает в убыток.')
    print(f'\nСредняя прибыль по компаниям: {round((total_profit / company_counter), 2)}\n')
    average_profit_dict['average_profit'] = round((total_profit / company_counter), 2)

    dicts_list.append(companies_profit_dict)
    dicts_list.append(companies_loss_dict)
    dicts_list.append(average_profit_dict)

    return dicts_list


with open('file_for_DZ5-7.txt', encoding='utf-8') as text:
    my_list = [line.split() for line in text]
    with open('json.txt', 'w') as json_file:
        json.dump(short_info(my_list), json_file)
