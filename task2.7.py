def func(numb):
    if numb == 1:
        return numb
    else:
        return func(numb - 1) + numb


my_num = int(input("Enter the number: "))
if func(my_num) == my_num * (my_num + 1) / 2:
    print("Equality is true")
