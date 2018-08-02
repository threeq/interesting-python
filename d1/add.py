
def add(a, b):
    return a+b


def add_3(a, b, c):
    return a+b+c


def add_n1(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result


def add_n2(*numbers):
    return sum(numbers)
