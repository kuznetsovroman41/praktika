a = int(input("Введите число a: "))

for i in range(1, a + 2):
    if i * i > a:
        print("Первое число больше a:", i * i)
        break


b = int(input("Введите число b: "))

num = 1
step = 4

while num <= b:
    num = num + step
    step = step + 1

print("Первое число больше b:", num)