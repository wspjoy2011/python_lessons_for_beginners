# while condition: заголовок цикла, последовательность операторов и функций - тело цикла

print(sum(number for number in range(1000 + 1)))

number = 1000
count = 0
result = 0

while count <= number and count <= 50:
    result += count
    count += 1

print(result)

password = 'password'
user_password = ''
count = 0

while user_password != password and count < 3:
    user_password = input('Введите пароль: ')
    if user_password == password:
        break
    count += 1

if count == 3:
    print('Превышено число попыток')
else:
    print('Добро пожаловать')

