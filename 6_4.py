list = [True, 5, 'go', 3 + 0.1j]

print("Исходный список:", list)

last = list[-1]

for i in range(len(list) - 1, 0, -1):
    list[i] = list[i - 1]

list[0] = last

print("После сдвига:", list)