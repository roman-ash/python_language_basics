class Matrix:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'Matrix: {self.data}'

    def __add__(self, other):
        result_matrix = []
        for i, row in enumerate(self.data):
            result_matrix.append([])
            for j, column in enumerate(row):
                result_matrix[i].append(0)
                result_matrix[i][j] = self.data[i][j] + other.data[i][j]
        return Matrix(result_matrix)


m1 = Matrix([[6, 1, 7], [3, 1, 4], [9, 5, 8]])
m2 = Matrix([[5, 9, 4], [7, 5, 1], [0, 2, 3]])
print(m1)
m3 = m1 + m2
print(m3)
