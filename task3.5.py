sum_result = 0
i = True
while i:
    try:
        numbers = input("Введите числа через пробел. Для выхода введите q\n: ").split()
        result = 0
        for number in range(len(numbers)):
            if numbers[number] == "q" or numbers[number] == "Q":
                i = False
                break
            else:
                result += int(numbers[number])
        sum_result += result
        print(f"Текущая сумма: {sum_result}")
    except ValueError:
        print("Введите числа!")
print(f"Финальная сумма: {sum_result}")
