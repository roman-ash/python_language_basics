from sys import argv

script_name, prodh, rateh, prem = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", prodh)
print("Ставка в час: ", rateh)
print("Премия: ", prem)
print("Заработная плата: ", (int(prodh) * int(rateh)) + int(prem))
