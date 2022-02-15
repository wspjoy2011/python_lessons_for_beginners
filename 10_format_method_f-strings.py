name = 'John'
age = 30
# f'string' - позволяет выполнять код и выводить переменные внутри строки
print(f'Name: {name}, age: {age}')
# метод формат в {} указываем индекс переданого аргумента
print('Name: {0}, age: {1}.\nHave a nice day {0}.'.format(name, age))
print('Name: {name}, age: {age}.\nHave a nice day {name}.'.format(name=name, age=age))

