# list[start:stop:step], slice(start:stop) - срезы работают аналогичным образом со строками, срез возвращает новый объект
cities = ['Tokyo', 'Madrid', 'London', 'New-York']
print(cities[1:3])
# list[:], list(list_name) - копия списка
new_cities = cities[:]
new_cities = list(cities)
print(id(cities), id(new_cities))
print(new_cities[1::2])
print(new_cities[::2])
# изменение списка по срезу
new_cities[2:4] = 'Kiev', 'Beijing'
print(new_cities)
# += [value], lst.append(value) - добавить элемент в конец списка
new_cities += ['Singapore']
print(new_cities)
# > < != == - сравнение списков
print([1, 2, 3] < [2, 3, 4])
