from random import randint
# break - прервать цикл
# continue - пропуск одной итерации
numbers = [randint(1, 1000) for _ in range(50)]
count = 0
while count < len(numbers):
    if numbers[count] % 2 == 0:
        print(numbers[count], count)
        break
    count += 1

count = 0
while count < len(numbers) and numbers[count] % 2 == 0:
    count += 1

result = 0
count = 0


while count < len(numbers):
    if numbers[count] % 2 != 0:
        count += 1
        continue
    result += numbers[count]
    count += 1

print(result)

# else выполняется при штатном завершении цикла, штатное завершение цикла по заголовку цикла

result = 0
i = -10

while i < 100:
    if i == 0:
        break  # нештатное завершение цикла
    result += 1 / i
    i += 1
else:
    print('Сумма вычислена корректно.')

print(result)

