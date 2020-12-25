x = int(input("Введите кол-во наименований товара: "))

my_list = []

names_list = []
prices_list = []
quantity_list = []
units_list = []

for i in range(x):
    name = input(f"Введите название {i + 1}-ого товара: ")
    names_list.append(name)
    price = int(input(f"Введите цену {i + 1}-ого товара: "))
    prices_list.append(price)
    quantity = int(input(f"Введите кол-во {i + 1}-ого товара: "))
    quantity_list.append(quantity)
    unit = input(f"Введите ед. измерения {i + 1}-ого товара: ")
    units_list.append(unit)
    products = (i + 1, dict([("название", name), ("цена", price), ("кол-во", quantity), ("ед.", unit)]))
    my_list.append(products)

print(my_list)

analytics = dict([("название", names_list),
                 ("цена", prices_list),
                 ("кол-во", quantity_list),
                 ("ед.", units_list)])
print(analytics)
