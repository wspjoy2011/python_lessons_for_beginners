# словарь упорядоченная коллекция
temps = ['+7', '+6', '+5', '+4']
# dict.fromkeys(lst) - создаёт словарь с ключами взятыми из коллекции и значениями None
temps = dict.fromkeys(temps)
print(temps)
# вторым аргументом передаём значение по умолчанию
temps = dict.fromkeys(['+7', '+6', '+5', '+4'], 0)
print(temps)
# dict.clear() - очистка словаря
temps.clear()
print(temps)

temps = {
    'house': 'дом', 'tree': 'дерево',
    'car': 'машина', 'road': 'дорога'
}

# dict.copy() возвращает копию словаря
temps_copy = temps.copy()
print(temps_copy)
temps_copy1 = dict(temps_copy)
print(temps_copy1)
# dict.get(key, default_value) - получить значение по ключу
print(temps.get('house'))
print(temps.get('cat', 0))
# dict.setdefault(key, default_value) - если ключа нету в словаре то создаётся ключ по значением переданным вторым аргументов
# если ключ есть в словаре то вернёт его значение
print(temps.setdefault('house'))
temps.setdefault('cat')
print(temps)
# dict.pop(key, default) - удаляет из словаря по ключу, если ключ не найден вернёт значение вт орого аргумента
temps.pop('cat')
print(temps)
temps.pop('town', None)
# dict.popitem() - удаляет последнюю пару в словаре
temps.popitem()
print(temps)
# dict.keys() - возвращает список ключей
print(list(temps_copy1.keys()))

for key in temps_copy1:
    print(f'{key} = > {temps_copy1[key]}')

# dict.values() - список значений
print(list(temps_copy1.values()))

#dict.items() - возвращает список кортежей ключ, значение
print(list(temps_copy1.items()))

for key, value in temps_copy1.items():
    print(f'{key} => {value}')

# dict.update(other_dict) - обновляет/дополняет словарь dict с помощью пар ключ-значение из other
temps = {'+7': 0, '+6': 0, '+5': 0, '+4': 0}
temps.update(temps_copy1)
print(temps)
# {**dict1 + **dict2} - объедениние словарей
new_dict = {**temps, **temps_copy1}
# аналогично dict1 | dict2
print(temps | temps_copy)
