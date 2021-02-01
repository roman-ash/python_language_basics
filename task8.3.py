class OnlyInt(Exception):
    def __init__(self, txt):
        self.txt = txt


c = 1
my_list = []
while True:
    a = input(f"Input item {c}. Input 'stop' to stop generating the list.\n: ")
    if a == "stop":
        print(my_list)
        break
    try:
        a = int(a)
        if type(a) != int:
            raise OnlyInt("Only numbers")
    except (ValueError, OnlyInt) as err:
        print(err)
    else:
        my_list.append(a)
        c += 1
    finally:
        print(my_list)
