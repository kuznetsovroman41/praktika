from math import tan, fabs

months = [
    "Январь", "Февраль", "Март", "Апрель",
    "Май", "Июнь", "Июль", "Август",
    "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
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
    u = 3*x - 2*x/fabs(x)
else:
    u = 6 * tan(13 - 3*x**2)**3

print(u)