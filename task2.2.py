def even_and_odd(num, even=0, odd=0):
    if num == 0:
        return even, odd
    else:
        cur_num = num % 10
        num = num // 10
        if cur_num % 2 == 0:
            even += 1
        else:
            odd += 1
        return even_and_odd(num, even, odd)


print(even_and_odd(12332))
