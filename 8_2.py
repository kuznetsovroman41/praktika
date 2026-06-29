def product(arr):
    p = 1
    for x in arr:
        p *= x
    return p


def average(arr):
    return sum(arr) / len(arr)


for i in range(1, 4):
    n = int(input(f"Введите количество элементов {i}-го массива: "))

    arr = []
    print("Введите элементы:")
    for j in range(n):
        arr.append(int(input()))

    print("Массив:", arr)
    print("Произведение элементов:", product(arr))
    print("Среднее арифметическое:", average(arr))
    print()