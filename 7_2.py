n = int(input("Введите размер матрицы: "))

matrix = []

print("Введите элементы матрицы:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(float(input()))
    matrix.append(row)

max_abs = abs(matrix[0][0])
row_index = 0
col_index = 0

for i in range(n):
    for j in range(n):
        if abs(matrix[i][j]) > max_abs:
            max_abs = abs(matrix[i][j])
            row_index = i
            col_index = j

print("Исходная матрица:")
for row in matrix:
    print(row)

print("Максимальный по модулю элемент:", matrix[row_index][col_index])

new_matrix = []

for i in range(n):
    if i != row_index:
        new_row = []
        for j in range(n):
            if j != col_index:
                new_row.append(matrix[i][j])
        new_matrix.append(new_row)

print("Новая матрица:")
for row in new_matrix:
    print(row)