import numpy as np

n = int(input("Введите размер квадратной матрицы (n): "))
k = int(input("Введите число k для проверки кратности: "))

print(f"\nВведите элементы матрицы по очереди (всего нужно ввести {n * n} шт.):")

elements = [int(input()) for _ in range(n * n)]

matrix = np.array(elements).reshape(n, n)

multiples = matrix[matrix % k == 0]

print("\n--- Результаты ---")
print("Полученная матрица:")
print(matrix)


count = len(multiples)
print(f"\nКоличество элементов, кратных {k}: {count}")

if count > 0:
    print("Наибольший из этих элементов:", multiples.max())
else:
    print(f"Элементов, кратных {k}, в матрице не обнаружено.")