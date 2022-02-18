number = 10
factorial = 1

for num in range(1, number + 1):
    factorial *= num

print(factorial)

for mult in range(1, 10):
    print('*' * mult)

# ' '.join(words)
words = ['one', 'two', 'three']
sentence = ''

for word in words:
    sentence += f'{word} '

print(sentence.rstrip())

numbers = [1, 10, 99, 101, 100, 16, 7, -19]

for i in range(len(numbers)):
    if 100 > abs(numbers[i]) > 9:
        numbers[i] = 0

print(numbers)
# enumerate(lst) - возвращает список кортежей (index, value)
print(list(enumerate(numbers)))
for index, value in enumerate(numbers):
    print(f'{index}: {value}')
