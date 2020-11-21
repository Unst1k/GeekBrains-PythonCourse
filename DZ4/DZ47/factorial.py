def fact_number(number):
    for any_number in range(1, number + 1):
        yield any_number


def total_number(number):
    factorial = 1
    numbers_list = []
    for i in number:
        numbers_list.append(i)
        factorial *= i
    print(f'!{numbers_list[-1]} = {" * ".join(str(i) for i in numbers_list)} = {factorial}.')
