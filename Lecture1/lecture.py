print('hello world')

value = None
print(type(value))

a = 123            # целое число
b = 1.23           # плавающая точка
print(type(a))
print(type(b))
value = 12345
print(type(value))
s = 'hello world'     # строка

print(s)
print(a, '-', b, '-', s)

# основные форматы выводов:
print('{} - {} - {}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s))     # вывод по индексу
print(f'{a} - {b} - {s}')                    # интерполяция

f = True      # логическая переменная
print(f)

# списки (как массивы в C#):
list = [1, 2, 3]
list = ['1', '2', '3', 'hello', 1, 2, 4.5, True]
print(list)

# ввод вывод данных:
print('Введите a')
a = int(input())
print('Введите b')
b = int(input())
print(a, '+', b, '=', a + b)
print('{} {}'.format(a, b))
print(f'{a} {b}')

# арифметические операции:
a = 3 
a = 3 + 5   # a += 5   

b = 3
c = a / b     # дробное деление
c = a // b    # целочисленное деление (без цифры после запятой)
c = a % b     # получение остатка от деления
c = a ** b    # возведение в степень
c = round(a * b, 5)    # вывод количества знаков после запятой
print(a)


# логические операции:
a = 1 < 4 and 5 > 2
print(a)
a = 'qwe'       # сравниваем строки
b = 'qwe'
print(a == b)
a = [1, 2]        # сравнение по элементам списка
b = [1, 2]
print(a == b)
a = 1 < 3 < 5 < 10   # множественное неравенство
print(a)
func = 1
T = 4
x = 123
print(func<T>x)     # просто) множественное неравенство
f = 1 > 2 or 4 < 6   # коньюкция, дизьюнкция (or) если верно хоть одно неравенство. то "true"
print(f)
f = [1,2,3,4]
print(f)
print(2 in f)        # подтверждение
print(not 2 in f)    # отрицание

is_odd = f[0] % 2 == 0
is_odd = not f[0] % 2   # так лучше писать
print(is_odd)

# управляющие конструкции if, if-else:
a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина! ')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ',username)

# управляющие конструкции while, for:
# инвертирование числа
original = 23 
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй хватит')
print(inverted)

for i in 1,2,3,4,5:     # возведение в степень
    print(i**2)

r = range(10)    # все числа от 0 до 10
for i in r:
    print(i)
for i in range(4):
    print(i)






