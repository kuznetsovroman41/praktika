A = []
B = []

print("Введите элементы массива A:")
for i in range(10):
    A.append(int(input()))

print("Введите элементы массива B:")
for i in range(10):
    B.append(int(input()))

print("Исходный массив A:", A)
print("Исходный массив B:", B)

A, B = B, A

print("Преобразованный массив A:", A)
print("Преобразованный массив B:", B)