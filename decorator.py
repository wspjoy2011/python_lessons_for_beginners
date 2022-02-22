from datetime import datetime

def wrapper(func):
    def inner():
        print('start decorator...')
        func()
        print('end decorator...')
    return inner


def say_hello():
    print('Hello, world!')


d = wrapper(say_hello)
print(d)
d()  # замыкание

say_hello = wrapper(say_hello)  # декоратор, название переменной должно совпадать с названием функции
say_hello()

# Следующий пример с функцией которая принимает аргументы
def wrapper(func):
    def inner(*args, **kwargs):
        print('start decorator...')
        func(*args, **kwargs)
        print('end decorator...')
    return inner


def measure_time(func):
    def inner(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        a = 2**100000000
        finish = datetime.now()
        print(f'{finish.second - start.second}.{abs(finish.microsecond - start.microsecond)}')
    return inner


@measure_time
@wrapper  # синтаксический сахар
def say_hello(name, surname):
    print(f'Hello, {name} {surname}!')


# say_hello = measure_time(wrapper(say_hello))
say_hello('John', 'Smith')


