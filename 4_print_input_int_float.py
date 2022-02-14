# функция print вывод данных в консоль
print(1, 2, 3, sep=' | ', end=' #\n')
# f-строка и print
x = 10
y = -1
print(f'Координаты точки: x = {x}, y = {y}.')
# input - ввод значения с клавиатуры
# name = input('Введите своё имя: ').title()
# print(f'Имя: {name}', type(name))
# print(abs(int(input('Введите число: '))))
a, b = map(float, input('Введите две стороны прямоугольника: ').split())
print(f'Периметр прямоугольника: {2 * (a + b)}')
