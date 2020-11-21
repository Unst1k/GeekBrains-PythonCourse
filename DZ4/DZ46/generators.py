from itertools import count, cycle


def numbers_generator(user_number, last_number):
    for i in count(user_number):
        if i > last_number:
            break
        else:
            print(i)


def row_generator(user_row, repeat):
    row_count = 0
    for i in cycle(user_row):
        if row_count > (repeat*len(user_row)-1):
            break
        print(i)
        row_count += 1
