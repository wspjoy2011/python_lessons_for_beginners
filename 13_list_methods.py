numbers = [-1, 24, 17, 9, -31, 0]
# lst.append(value) добавить элемент в конец списка
numbers.append(10)
print(numbers)
# lst.insert(index, value) добавить элемент в список по указаному индексу
numbers.insert(1, True)
print(numbers)
# lst.remove(value) - удалить элемент по значению, если значения нет в списке вызывается исключение ValueError
numbers.remove(True)
print(numbers)
# lst.pop() - удаляет последний элемент и возвращает его, если указать индекс то удаляет по нему
value = numbers.pop()
print(numbers, value)
value = numbers.pop(0)
print(numbers, value)
# lst.clear() - возвращает пустой список
# lst.copy() - копия списка
# lst.count(value) - возвращает число найденых элементов
print(numbers.count(9))
# lst.index(value, start) - возвращает индекс первого совпадающего элемента, если значения нет в списке вызывается исключение ValueError
print(numbers.index(9))
print(numbers.index(9, 1))
# lst.revers() - реверс элементов списка
numbers.reverse()
print(numbers)
# lst.sort() - сортировка списка
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)






