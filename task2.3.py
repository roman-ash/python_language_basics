def reverse_num(num, re_num=''):
    if num == 0:
        return re_num
    else:
        cur_num = num % 10
        num = num // 10
        re_num += str(cur_num)
        return reverse_num(num, re_num)


print(reverse_num(120340))
