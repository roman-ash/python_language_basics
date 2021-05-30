def my_min1(lst):
    # O(N^2)
    min_num1 = 0                             # O(1)
    for i in range(len(lst)):                # O(N)
        for j in lst:                        # O(N^2)
            if lst[i] > j and min_num1 > j:  # O(1)
                min_num1 = j                 # O(1)
    return min_num1                          # O(1)


def my_min2(lst):
    # O(N)
    min_num2 = lst[0]     # O(1)
    for i in lst:         # O(N)
        if min_num2 > i:  # O(1)
            min_num2 = i  # O(1)
    return min_num2       # O(1)


print(my_min2([3, 6, 9, 0, 1, 8]))
print(my_min1([3, 6, 9, 0, 1, 8]))
