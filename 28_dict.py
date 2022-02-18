dictionary = {
    'house': 'дом', 'tree': 'дерево',
    'car': 'машина', 'road': 'дорога'
}
print(dictionary)
print(dictionary['house'])
# обращение к несуществующему ключу вызовет исключение KeyError
print(dict(one=1, two=2, three='3', four='4'))

marks = [(2, 'bad'), (3, 'normal'), (4, 'good'), (5, 'great')]
marks = {item[1]: item[0] for item in marks}
print(marks)
print(dict(marks))
# len() - возвращает колличество элементов словаря
print(len(marks))
# del dict[key] - удаляет пару ключ: значение
del marks['bad']
print(marks)
# value in dict - проверка на вхождение ключа
print('good' in marks)
print('good' not in marks)
