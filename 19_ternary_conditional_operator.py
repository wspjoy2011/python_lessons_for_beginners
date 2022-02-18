a = 12
b = 7

if a > b:
    result = a
else:
    result = b
print(result)

# тернарный оператор value if condition else value
result = abs(a) + 2 if a > b else abs(b) - 1
print(result)

func = lambda x: print(f'{x} - чётное') if x % 2 == 0 else print(f'{x} - нечётное')
numbers = [1, 22, 30, 55, 0]
for number in numbers:
    func(number)

language = 'python'
mark = 'upper'
result = language.upper() if mark == 'upper' else language
print(result)

numbers = [1, 2, a if a < b else b, 4, 5]
print(numbers)
print('a -', ('чётное' if a % 2 == 0 else 'нечётное'), 'число')
print(max(1, 5, a if a > 0 else b, -1, 6))
# наибольшее из трёх чисел

a, b, c = 2, 3, -4
d = (a if a > c else c) if a > b else (b if b > c else c)
print(d)
