# for variable in iterable, аналог for each
numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    print(number)

for letter in 'python':
    print(letter)

result = 1

for number in numbers:
    result *= number

print(result)

for index in [1, 2, 3, 4, 5]:
    numbers[index] = 0
print(numbers)

# range(start:stop:step) - функция генератор

print(list(range(5)))
print(list(range(-10, -3, 2)))
print(list(range(-10, -20, -2)))
