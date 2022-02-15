string1 = 'python'
# перевод строки в верхний регистр
print(string1.upper())
print(string1.upper.__call__())
# перевод в нижнимй регистр
print(string1.lower())
# str.count(substring, start, end) - возвращает число сколько раз подстрока встречается в строке, end не входит в поиск
print(string1.count('yt', 0, len(string1)))
# str.find(substring, start, end) - возвращает индекс первого вхождения подстроки
print(string1.find('h'))
# str.rfind() - тоже что и find, только поиск осуществляется справа на лево
print(string1.rfind('h'))
# str.index(substring, start, end) - возвращает индекс первого вхождения, если не находит - вызывает исключение ValueError
print(string1.index('o'))
# str.replace(old, new, count=-1) - -1 значит что будут замены без ограничений по колличеству
print(string1.replace('p', 'l'))
print(string1.replace('p', ''))
# str.isalpha() возвращает истину если строка состоит из буквеных символов
print(string1.isalpha())
# str.isalpha() возвращает истину если строка состоит из цыфр
print('777'.isdigit())
# str.rjust() функция возвращает строку выравненную по правому краю в строке по ширине.
print(string1.rjust(10))
print(string1.rjust(10, '*'))
# str.ljust() работает аналогичным образом
# str.split(sep=None, maxsplit=-1) разбивает строку по символу сепаратора
print('1 2 3 4'.split())
digits = '1, 2,3, 4,   5,6'
print(digits.replace(' ', '').split(','))
# str.join(array) - возвращает строку из коллекции
print(', '.join(['john', 'dow', 'hawk']).title())
full_name = 'Jonh Doe'
print(', '.join(full_name.split()))
# str.split() - удаляет все символы пробелов и переноса строк в начале и в конце строки
print('  test  \n'.strip())
# str.rstrip(), str.lstrip() - делает тоже самое только справа и слево

