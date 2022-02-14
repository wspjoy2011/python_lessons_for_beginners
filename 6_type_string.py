# метод title возвращает новую строку с заглавной первой буквой
first_name = 'john'.title()
last_name = 'doe'
# конкатенация строк
print(f'{first_name} {last_name.title()}')
# многострочная строка
text = '''
first line
second line
'''
print(text)
space = ' '
string1 = 'I love'
string2 = 'Python'
print(string1 + space + string2)
# приведение к строковому типу
print(string1 + space + str(5))
print(str(True))
# мультипликация строк
print((string2 + space) * 5)
# len() - длинна строки
print(f'Length {string2}: {len(string2)}')
# оператор in проверяет вхождение подстроки в строку
print('thon' in string2)
# == проверка на равенство строк
print('python' == string2)
# лексикографическое сравнение строк с операторами < >
print('AAA' > 'zzz')
# функция ord() для символа вернет число, из таблицы символов Unicode
print(ord('A'), ord('a'))
