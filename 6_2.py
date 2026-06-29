n = int(input("Введите количество элементов первого массива: "))
m = int(input("Введите количество элементов второго массива: "))

arr_1 = []
arr_2 = []

for i in range(n):
    arr_1.append(int(input(f"Введите элемент первого массива {i + 1}: ")))

for e in range(m):
    arr_2.append(int(input(f"Введите элемент второго массива {e + 1}: ")))

print(arr_1)
print(arr_2)