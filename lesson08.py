# Множество - элементы не повторяются
a = set(['1', '2', '3', '2'])
# Вывести множество
print(a) # {'1', '3', '2'}
# Проверка на вхождение элемента в множество
if '1' in a:
  print("1 есть в множестве a") # 1 есть в множестве a
# Скопировать множество
b = a.copy()
# Добавить в множество b элемент '4'
b.add('4')
# Проверить является ли множество b подмножеством a
print(b.issuperset(a)) # True
# Удалить элемент '1' из множества a
a.remove('1')
# Пересечение множеств
print(a&b) # {'3', '2'}
# Тоже пересечение множеств
print(a.intersection(b)) # {'3', '2'}
