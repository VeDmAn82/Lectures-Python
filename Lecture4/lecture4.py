# Метод инициализации начальных значений х, у

x = 0
y = 0

def init(a, b):
    global x
    global y
    x = a
    y = b

init(11, 22)

print(x)
print(y)


# Метод действия (+, -, /, *)

def sum():
    return x + y
