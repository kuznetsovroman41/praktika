import numpy as np

n = int(input("Количество элементов: "))
arr = np.array([int(input(f"Элемент {i+1}: ")) for i in range(n)])

min_elem = arr[np.abs(arr).argmin()]
print("Минимальный по модулю:", min_elem)

print("В обратном порядке:", arr[::-1])