def my_func(num1, num2, num3):
    nums_list = [num1, num2, num3]
    nums_list.remove(min(nums_list))
    return sum(nums_list)


print(my_func(10, 5, 7))
