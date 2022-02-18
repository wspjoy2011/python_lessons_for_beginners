x = 10

if isinstance(x, (int, float)):
    if x < 0:
        print(f'Число {x} - положительное')
    else:
        print(f'Число {x} - отрицатильное')

else:
    print(f'{x} - не является числом')

# поиск наибольшего числа из трёх
a, b, c = 1, 2, 3

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(c)
else:
    print(c)
