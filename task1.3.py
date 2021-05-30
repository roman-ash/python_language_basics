def top3_1(my_dict):
    # O(N^2)
    my_list = list(my_dict.items())            # O(N)
    le = len(my_list)                          # O(1)
    for i in range(le - 1):                    # O(N)
        for j in range(i + 1, le):             # O(N^2)
            if my_list[i][1] > my_list[j][1]:  # O(1)
                t = my_list[i]                 # O(1)
                my_list[i] = my_list[j]        # O(1)
                my_list[j] = t                 # O(1)
    return dict(my_list[-3:])                  # O(N)


def top3_2(my_dict):
    # O(N log N)
    my_list = sorted(my_dict.items(), key=lambda x: x[1])  # O(N log N)
    return dict(my_list[-3:])                              # O(N)


# Решение под номером 2(top3_2) эффективнее, так как линейно-логирифмическая функция быстрее квадратичной.
print(top3_1({'ABC': 5000, 'BBC': 2500, 'CNN': 6000, 'FOX': 4000, 'NBA': 3000}))
print(top3_2({'ABC': 5000, 'BBC': 2500, 'CNN': 6000, 'FOX': 4000, 'NBA': 3000}))
