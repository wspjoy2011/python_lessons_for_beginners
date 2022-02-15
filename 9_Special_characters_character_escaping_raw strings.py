# \n - символ перевода строки(newline) длинна от len() - один символ
text = 'hello\npython'
print(text)
# \t - символ табуляции(размером четыре пробела)
print('\t' + text)
# \\ - обратный слеш
print('\\' + text)
# \', \" - одинарные, двойные кавычки
# r'string' - raw строка вывод всех символов(ескейп последовательности)
text = r'hello\npython'
print(text)
