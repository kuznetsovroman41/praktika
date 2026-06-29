n = int(input("Введите размер матрицы: "))
k = int(input("Введите число k: "))

matrix = []

print("Введите элементы матрицы:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)

count = 0
max_elem = None

for i in range(n):
    for j in range(n):
        if matrix[i][j] % k == 0:
            count += 1
            if max_elem is None or matrix[i][j] > max_elem:
                max_elem = matrix[i][j]

print("Матрица:")
for row in matrix:
    print(row)

print("Количество элементов, кратных", k, "=", count)

if count > 0:
    print("Наибольший кратный элемент:", max_elem)
else:
    print("Элементов, кратных", k, "нет.")