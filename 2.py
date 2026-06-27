from math import log, tan, sin
a = int(input("Введите первое число: "))
b = int(input("Введите втрое число: "))
y = int(input("Введите третье число: "))
x = int(input("Введите четвертое число: "))

t1 = (1 / b**2) * (log(a / x) + (a * x) / y)

t2 = (x / a) * tan((a * x) / 2) + (2 / a**2) * log(sin((a * x) / 2))

print(t1)
print(t2)