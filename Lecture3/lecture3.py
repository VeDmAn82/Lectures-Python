# Анонимные lambda функции

# def sum(x):
#     return x+10
# def mult(x):
#     return x**2
# sum(mult(2))

# def sum1(x):
#     return x+22
# def mult2(x):
#     return x**3
# sum1(mult2(2))

# def sum3(x):
#     return x+242
# def mult4(x):
#     return x**5
# sum3(mult2(2))

# sum = lambda x: x+10
# mult = lambda x: x**2
# sum(mult(2))

# sum1 = lambda x: x+22
# mult2 = lambda x: x**3
# sum1(mult2(2))

# sum4 = lambda x: x+242
# mult4 = lambda x: x**5
# sum3(mult2(2))

# f(g(x))
# def h(f, g, x): 
#     return f(g(x))
# h = lambda f, g, x:f(g(x))
# h(sum, mult, 5)
# h(lambda x: x+10, lambda x: x**2, 5)

# В файле f.txt хранятся числа (1,2,3,5,8,15,23,38), нужно выбрать четные и
# составить список пар (число; квадрат числа):

# Вариант1:
# f = open('f.txt', 'r')
# data = f.read() + ' '
# f.close()
# numbers = []
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]
# out = []
# for e in numbers:   
#     if not e % 2:
#         out.append((e, e **2))
# print(out)

# Вариант2:
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)                    
# res = where(lambda x: not x % 2, res)
# res = select(lambda x:(x, x**2), res)

# data = '1 2 3 5 8 15 23 38'.split()               # Решение через объект "map", функция "select" - не нужна
# res = map(int, data)
# res = where(lambda x: not x % 2, res))
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# data = '1 2 3 5 8 15 23 38'.split()                  # Решение через "filter"
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res)

# ФУНКЦИЯ map
# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
# f(x) ⇒ x + 10
# map(f, [ 1, 2, 3, 4, 5])
#  ↓ ↓ ↓ ↓ ↓
#  [ 11, 12, 13, 14, 15]
# Нельзя пройтись дважды

# Пример:
# li = [x for x in range(1, 21)]
# li = list(map(lambda x:x+10, li))
# print(li)

# Пример2:
# data = list(map(int,input().split()))   # List - принудительное сохранение в список, для дальнейшей работы
# print(data)

# ФУНКЦИЯ filter

# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4,5])
#  ↓
#  [ 2, 4 ]
# Нельзя пройтись дважды

# ФУНКЦИЯ zip

# Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами из
# элементов входных данных. Количество элементов в результате равно минимальному количеству элементов входного набора
# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#  ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды

# Пример:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14,7]
# data = list(zip(users, ids))
# print(data)


# ФУНКЦИЯ enumerate

# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#  ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды

# Пример:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14,7]
# data = list(enumerate(users))
# print(data)


# List Comprehension
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# Пример:
# list = [i for i in range(1, 21) if i % 2 == 0]
# print(list)                                       # вывод списком

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)                                       # вывод кортежем(число и его куб)

