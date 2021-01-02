from itertools import count
from itertools import cycle

for el in count(3):  # a
    if el > 10:
        break
    else:
        print(el)

c = 0
for i in cycle("AJAV"):  # b
    if c > 10:
        break
    print(i)
    c += 1
