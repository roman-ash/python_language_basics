with open("text_5.txt", "w") as f:
    f.write("1 3 5 7 9")
with open("text_5.txt", "r") as x:
    sum_nums = 0
    for line in x:
        for nums in line:
            if nums != ' ':
                sum_nums += int(nums)
    print(sum_nums)
