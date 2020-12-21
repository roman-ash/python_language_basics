time = int(input("Введите время в секундах: "))
hours = (time // 3600) % 24
minutes = (time // 60) % 60
seconds = time % 60
print(f"{hours}:{minutes}:{seconds}")
