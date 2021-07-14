from random import randint
from timeit import timeit


def merge(left_lst, right_lst):
    sorted_lst = []
    left_lst_index = right_lst_index = 0

    left_lst_length, right_lst_length = len(left_lst), len(right_lst)

    for _ in range(left_lst_length + right_lst_length):
        if left_lst_index < left_lst_length and \
                right_lst_index < right_lst_length:
            if left_lst[left_lst_index] <= right_lst[right_lst_index]:
                sorted_lst.append(left_lst[left_lst_index])
                left_lst_index += 1
            else:
                sorted_lst.append(right_lst[right_lst_index])
                right_lst_index += 1
        elif left_lst_index == left_lst_length:
            sorted_lst.append(right_lst[right_lst_index])
            right_lst_index += 1
        elif right_lst_index == right_lst_length:
            sorted_lst.append(left_lst[left_lst_index])
            left_lst_index += 1
    return sorted_lst


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)


my_list = [randint(-100, 100) for i in range(1000)]
print(timeit("merge_sort(my_list[:])", globals=globals(), number=100))
