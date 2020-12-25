month = int(input("Введите номер месяца: "))

my_dict = {1: "winter",
           2: "winter",
           3: "spring",
           4: "spring",
           5: "spring",
           6: "summer",
           7: "summer",
           8: "summer",
           9: "autumn",
           10: "autumn",
           11: "autumn",
           12: "winter",
           }
print(my_dict.get(month))

my_list = ["winter",
           "winter",
           "spring",
           "spring",
           "spring",
           "summer",
           "summer",
           "summer",
           "autumn",
           "autumn",
           "autumn",
           "winter"
           ]
print(my_list[month + 1])
