n = int(input("Введите количество элементов: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Введите элемент {i + 1}: ")))

min_elem = arr[0]

for x in arr:
    if abs(x) < abs(min_elem):
        min_elem = x

print("Минимальный по модулю элемент:", min_elem)

arr.reverse()

print("Массив в обратном порядке:")
print(arr)