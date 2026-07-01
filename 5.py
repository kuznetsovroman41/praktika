text_1 = input("Введите текст: ")
word = input("Введите слово, которое нужно посчитать: ")

found_text = text_1.count(word)
print("Количество: ", found_text)

text_2 = input("Введите текст: ")
old = input("Что заменить: ")
new = input("На что заменить: ")

text = text_2.replace(old, new)
print("Результат:", text)