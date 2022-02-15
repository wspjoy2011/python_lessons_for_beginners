# список - упорядоченная коллекция данных
# для объявления списка используем литерал []
cities = ['Tokyo', 'Madrid', 'London']
marks = [2, 3, 4, 5, 3, 1, 4]
# sum сумма всех элементов
print(round(sum(marks) / len(marks), 1))
# изменение элементов по индексу
marks[0] = 5
# так как в массиве мы храним только ссылки на объекты, то коллекция может состоять из любых типов данных
marks[1] = 'good'
# функция list() возвращает новый список
letters = list('python')
print(letters)
# max(), min() - возвращает максимальное, минимальное значение из коллекции состоящей из объектов типа int, float
marks[1] = 2
print(max(marks), min(marks))
print(max(letters))
# sorted(list, reverse=False) - возвращает отсортированный список, не меняя исходный
print(sorted(marks))
# + объеденение списков
print(marks + letters)
# * мультипликация списка
print(letters * 2)
# in проверка на вхождение элемента в список
print('p' in letters)
# del list[index] удаление элемента массива
del letters[0]
print(letters)
