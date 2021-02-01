class MyZeroDivErr(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = input("Input dividend: ")
divisor = input("Input divisor: ")

try:
    dividend = int(dividend)
    divisor = int(divisor)
    if divisor == 0:
        raise MyZeroDivErr("Divisor cannot be zero")
except (ValueError, MyZeroDivErr) as err:
    print(err)
else:
    print(round(dividend / divisor, 2))
