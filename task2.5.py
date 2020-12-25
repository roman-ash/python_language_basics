my_list = [7, 5, 3, 3, 2]
a = int(input("Введите число: "))
b = 0
for i in my_list:
    if a >= i:
        my_list.insert(b, a)
        break
    elif a < my_list[-1]:
        my_list.append(a)
        break
    b += 1
print(my_list)
