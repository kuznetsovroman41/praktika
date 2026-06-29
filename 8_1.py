def sum_digits(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s


def count_steps(num):
    count = 0
    while num > 0:
        num -= sum_digits(num)
        count += 1
    return count


n = int(input("Введите число: "))
print("Количество действий:", count_steps(n))