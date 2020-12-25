string = input("Введите слова через пробел: ")
words = string.split()
count = 0
for i in words:
    count += 1
    print(f"{count}) {i[:10]}")
