# замыкание

def main_func(*args, **kwargs):
    name = args

    def inner_func():
        return f'Hello, ' + str(*name) + '!'

    return inner_func


func = main_func('John')
print(func)
print(main_func('Rich Franklin')())
print(func())


def adder(value_a):
    def inner(value_b):
        return value_a + value_b
    return inner


func = adder(10)
print(func(5))


def counter(limit):
    count = 0

    def inner():
        nonlocal count
        count += 1
        if count <= limit:
            return count
        return 'Out of limit!'

    return inner


c = counter(3)
print(c())
print(c())
print(c())
print(c())
