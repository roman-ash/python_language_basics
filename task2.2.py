my_list = []
x = int(input("Введите кол-во элементов списка: "))
for i in range(x):
    a = input(f"Введите {i + 1}-й элемент списка: ")
    my_list.append(a)
print(my_list)

c = 0
for b in range(int(len(my_list) / 2)):
    my_list[c], my_list[c + 1] = my_list[c + 1], my_list[c]
    c += 2
print(my_list)
