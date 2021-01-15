with open("text_3.txt", "r") as f:
    d = {}
    print("Has a salary of less than 20000:")
    for line in f:
        key, value = line.split()
        d[key] = value

    for key, value in d.items():
        if float(value) < 20000.0:
            print(key)

    salary_sum = 0
    count = 0
    for i in d.values():
        salary_sum += float(i)
        count += 1
    print(f"Average employee income: {round((salary_sum / count), 1)}")
