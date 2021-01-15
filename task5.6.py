with open("text_6.txt", "r") as f:
    d = {}
    for line in f:
        split_list = line.split()
        sum_nums = 0
        for word in split_list[1:]:
            cur_nums = 0
            for nums in word:
                if nums.isdigit():
                    cur_nums = int(str(cur_nums) + str(nums))
            sum_nums += cur_nums
        d[split_list[0].replace(":", "")] = sum_nums
    print(d)
