class Cell:
    def __init__(self, cell_num):
        self.cn = cell_num

    def __str__(self):
        return f"{self.cn}"

    def __add__(self, other):
        return Cell(self.cn + other.cn)

    def __sub__(self, other):
        return Cell(self.cn - other.cn)

    def __mul__(self, other):
        return Cell(self.cn * other.cn)

    def __truediv__(self, other):
        return Cell(round(self.cn / other.cn))

    def make_order(self, cells_in_row):
        my_str = ""
        for i in range(self.cn // cells_in_row):
            my_str += f"{'*' * cells_in_row} \n"
        my_str += f"{'*' * (self.cn % cells_in_row)}"
        return my_str


c1 = Cell(12)
c2 = Cell(2)
sum_cell = c1 + c2
sub_cell = c1 - c2
mul_cell = c1 * c2
div_cell = c1 / c2
print(sum_cell)
print(sub_cell)
print(mul_cell)
print(div_cell)
print(c1.make_order(5))
