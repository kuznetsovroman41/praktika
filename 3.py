from math import tan, fabs

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

month = int(input("Введите номер месяца (1-12): "))

if 1 <= month <= 12:
    print(months[month - 1])
else:
    print("Ошибка! Введите число от 1 до 12.")


x = float(input("Введите x: "))

if x < 0:
    u = x**2 - 3
elif x < 25:
    if x == 0:
        x = float(input("Ошибка! Введите x не равный 0: "))
    else:
        u = 3 * x - 2 * x / fabs(x)
        print(u)
else:
    u = 6 * tan(13 - 3*x**2)**3
    print(u)