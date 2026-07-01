import numpy as np

arr = np.random.randint(-100, 101, size=5)
print("Массив:", arr)

negatives = arr[arr < 0]

if len(negatives) > 0:
    print("Сумма отрицательных:", negatives.sum())
else:
    print("Отрицательных элементов нет")