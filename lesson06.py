# Список - изменяемый
list = ["Стол", "Диван", "Шкаф", "Кресло"]
# Узнать количество элементов в списке
print(len(list))
# Удалить элемент под индексом 1 (Диван)
del list[1]
# Добавить элемент
list.append("Стул")
# Сортировать список
list.sort()
# Обратиться к элементу по индексу
print("Элемента под индексом 0:", list[0])
# Вывести все элементы
for item in list:
  print(item)
# Объединить элементы списка в строку через разделитель
print("-".join(list))
# Генератор списка
numbers = [1,2,3,4,5,6,7,8]
# создать новый список, в котором четные элементы умножены на 2
numbers2 = [2 * i for i in numbers if i % 2 == 0]
print(numbers2) # [4, 8, 12, 16]

# Кортеж - не изменяемый, можно указывать без круглых скобок
cortej = ("Стол", "Диван", "Шкаф")

# Строки - не изменяемые
str = "ITDoctor"
# Начинается ли строка с "ITD"
print(str.startswith("ITD"))
# Есть ли подстрока "Doc" в строке str
print("Doc" in str)
# Индекс вхождения подстроки в строку
print(str.find("Doc"))
