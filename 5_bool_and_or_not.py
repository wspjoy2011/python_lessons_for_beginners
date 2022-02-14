# логический тип bool принимает True или False
a = 5
b = 7.8
print(a > b)
print(a < b)
result = a == b
print(result, type(result))
# операторы сравнения <, >, <=, >=, ==, !=
print(11 % 33)
print(7 == 5 + 2)
print(16 % 2 == 0)
print(-2 < a < b)
# оператор not инверсия условия
print(not(a % 2 == 0 or a % 3 == 0))
# приоритеты операторов чем выше тем больше приоритет
# not - 3, and - 2, or - 1
# функция bool() - преобразование аргумента в логический тип
print(bool(a))
print(bool(''))
