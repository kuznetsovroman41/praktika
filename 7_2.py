import numpy as np

n = int(input("Введите размер квадратной матрицы (n): "))

print(f"Введите элементы матрицы ({n * n} шт.):")
elements = [float(input()) for _ in range(n * n)]
matrix = np.array(elements).reshape(n, n)

row_index, col_index = np.unravel_index(np.abs(matrix).argmax(), matrix.shape)

print("\nИсходная матрица:")
print(matrix)
print(f"Максимальный по модулю элемент: {matrix[row_index, col_index]} (строка {row_index + 1}, столбец {col_index + 1})")

new_matrix = np.delete(matrix, row_index, axis=0)
new_matrix = np.delete(new_matrix, col_index, axis=1)

print(f"\nНовая матрица порядка {n - 1}:")
print(new_matrix)