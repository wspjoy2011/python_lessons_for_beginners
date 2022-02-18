numbers = [5, 7, 3, 10, 16]

# iter(iterable) - возвращает итератор для однократного перебора итерируемого объекта
iter_numbers = iter(numbers)
print(iter_numbers)

# next(iterator) - возвращает по одному объекты, когда мы дойдем до конца последовательности вызывается исключение StopIteration
# для того чтобы перебрать элементы заново, нужно создать новый итератор
print(next(iter_numbers))
print(next(iter_numbers))
print(next(iter_numbers))

string_iterator = iter('python')
print(next(string_iterator))
print(next(string_iterator))
print(next(string_iterator))

range_iterator = iter(range(5))
print(next(range_iterator))
