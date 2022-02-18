from timeit import timeit

# [value for _ in iterable]
square_numbers = [x * x for x in range(10)]
print(square_numbers)

odd_even = [x % 2 == 0 for x in range(20)]
print(odd_even)

even = [x for x in range(0, 20) if x % 2 == 0]
print(even)

python_ord = [ord(letter) for letter in 'python']
print(python_ord)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
# вложеное списковое включение
numbers = [number for row in matrix for number in row]
print(numbers)

even_odd = ['even' if number % 2 == 0 else 'odd' for number in numbers if number % 3 == 0]
print(even_odd)
print('sum([ ]) - ', timeit('sum([x*2 for x in range(100000)])', number=100))