import math
# модуль числа
print(abs(-10))
# наименьшее число в последовательности
print(min(1, 0, -2, 100))
# наибольшее число в последовательности
print(max(-1, 5, 17, 0))
# возведение числа в степень
print(pow(6, 2))
print(pow(49, 0.5))  # корень квадратный
print(pow(27, 1/3))  # корень кубический
# округление числа к ближайшему целому чётному числу
print(round(1.5))
# окрукление с указаной точностью
print(round(5.678956, 2))
# округление до десятков
print(round(784.54, -1))
# округление до сотен
print(round(784.54, -2))
# использование функции внутри других функций
print(max(1, 2, abs(-3), -10))
print(max(1, 2, abs(min(-1, -10, 5)), -10))
# посмотреть все функции модуля
print(dir(math))
# округление числа до наибольшего целого
print(math.ceil(10.1))
print(math.ceil(-5.7))
# округление до наименьшего целого
print(math.floor(5.9))
print(math.floor(-5.1))
# факториал числа
print(math.factorial(5))
# отбрасывание дробной части
print(math.trunc(5.9))
# тоже самое что и int
print(int(5.9))
# логарифм с основанием два
print(math.log(1000000000, 2))
# квадратный корень
print(math.sqrt(9))
# синус
print(math.sin(math.pi / 2))
# косинус
print(math.cos(10))
# основание натурального логарифма, математическая константа
print(math.e)

