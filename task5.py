proceeds = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
profit = proceeds - costs

if proceeds > costs:
    profitability = proceeds / profit
    print("Прибыль. Рентабельность выручки:", profitability)
else:
    print("Убыток")

staff = int(input("Введите количество персонала: "))
pDivs = profit / staff
print("Прибыль фирмы в расчете на одного сотрудника равна", pDivs)

