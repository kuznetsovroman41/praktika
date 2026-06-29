import random

arr = []

for i in range(5):
    arr.append(random.randint(-100, 100))

print("Массив:", arr)

sum_negative = 0
has_negative = False

for x in arr:
    if x < 0:
        sum_negative += x
        has_negative = True

if has_negative:
    print("Сумма отрицательных элементов:", sum_negative)
else:
    print("Отрицательных элементов нет")