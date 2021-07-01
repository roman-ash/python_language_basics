from collections import namedtuple

num_of_comp = int(input("Enter the number of companies: "))
companies = namedtuple(
    "Company",
    " name qr1 qr2 qr3 qr4")
average_profit = {}

for i in range(num_of_comp):
    company = companies(
        name=input("Enter company name: "), qr1=int(
            input("Enter first quarter profit: ")), qr2=int(
            input("Enter second quarter profit: ")), qr3=int(
            input("Enter third quarter profit: ")), qr4=int(
                input("Enter fourth quarter profit: ")))

    average_profit[company.name] = (
        company.qr1 + company.qr2 +
        company.qr3 + company.qr4) / 4

total_aver = 0
for value in average_profit.values():
    total_aver += value
total_aver = total_aver / num_of_comp

for key, value in average_profit.items():
    if value > total_aver:
        print(f"{key} - above average profit")
    elif value < total_aver:
        print(f"{key} - below average profit")
    elif value == total_aver:
        print(f"{key} - average profit")
