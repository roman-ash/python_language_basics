new_dict = {'as@gm.com': ['qwerty', True], 'dfg@gf.dg': ['4gdf', False]}


def new_act(login, password):
    # O(N)
    for i in new_dict:                                     # O(N)
        if i == login and new_dict[login][0] == password:  # O(1)
            if new_dict[login][1]:                         # O(1)
                return 'You are authenticated'
            else:
                return 'You are not authenticated'
    return 'Wrong login or password'


def new_act2(login, password):
    # O(1)
    if login in new_dict:                       # O(1)
        if new_dict.get(login)[0] == password:  # O(1)
            if new_dict.get(login)[1]:          # O(1)
                return 'You are authenticated'
            else:
                return 'You are not authenticated'
    else:
        return 'Wrong login or password'


# Решение "new_act2" эффективнее, так как константная функция быстрее и выполняется за построянное время
print(new_act('dfg@gf.dg', '4gdf'))
print(new_act('as@gm.com', 'qwerty'))
print(new_act('fghgh@fg', 'klk0'))
print('------')
print(new_act2('dfg@gf.dg', '4gdf'))
print(new_act2('as@gm.com', 'qwerty'))
print(new_act2('fghgh@fg', 'klk0'))
