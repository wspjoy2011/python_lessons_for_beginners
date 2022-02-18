x = -4
if x < 0:
    x = -x
print(x)

a = 4
b = 5
if a < b:
    a, b = b, a
print(a, b)

x = 5

if 0 < x < 10:
    print(f'0 < {x} < 10')

if x:
    print(x)

marks = [3, 3, 4, 2, 4]
if sum(marks) / len(marks) > 3:
    print('Средний бал: ' + str(sum(marks) / len(marks)))
else:
    print('Средний бал ниже входного порога')