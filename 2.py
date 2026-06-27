from math import log, tan, sin

a = int(input("Введите первое число: "))
while a == 0:
    a = int(input("Ошибка! Введите a ≠ 0: "))

b = int(input("Введите второе число: "))
while b == 0:
    b = int(input("Ошибка! Введите b ≠ 0: "))

y = int(input("Введите третье число: "))
while y == 0:
    y = int(input("Ошибка! Введите y ≠ 0: "))

x = int(input("Введите четвертое число: "))
while x == 0:
    x = int(input("Ошибка! Введите x ≠ 0: "))

t1 = (1 / b ** 2) * (log(a / x) + (a * x) / y)

sin_val = sin((a * x) / 2)

if sin_val > 0:
    t2 = (x / a) * tan((a * x) / 2) + (2 / a ** 2) * log(sin_val)
else:
    t2 = None
    print("Ошибка: логарифм не существует")

print("t1 =", t1)
print("t2 =", t2)