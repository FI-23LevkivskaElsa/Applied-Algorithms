from __future__ import annotations

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)
        for row in matrix:
            if len(row) != self.size:
                print("Помилка! Матриця має бути квадратною.")

    def add_matrix(self, other):
        if self.size != other.size:
            return print("Помилка! Матриці мають бути однакового розміру.")
        result = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def sub_matrix(self, other):
        if self.size != other.size:
            return print("Помилка! Матриці мають бути однакового розміру.")
        result = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def mul_matrix(self, other):
        if self.size != other.size:
            return print("Помилка! Матриці мають бути однакового розміру.")
        result = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                n = 0
                for k in range(self.size):
                    n = n + self.matrix[i][k] * other.matrix[k][j]
                row.append(n)
            result.append(row)
        return Matrix(result)

    def mul_vector(self, vector: Vector):
        if vector.size != self.size:
            return print("Помилка! Довжина вектора має дорівнювати розміру матриці.")
        result = []
        for i in range(self.size):
            n = 0
            for j in range(self.size):
                n = n + self.matrix[i][j] * vector.vector[j]
            result.append(n)
        return result

    def argmax(self, k):
        max_row = k
        max_value = self.matrix[k][k]
        for i in range(k, self.size):
            if self.matrix[i][k] > max_value:
                max_value = self.matrix[i][k]
                max_row = i
        return max_row

    def lup(self):
        P = [[1 if i == j else 0 for j in range(self.size)] for i in range(self.size)]
        for k in range(self.size):
            kk = self.argmax(k)
            if self.matrix[kk][k] == 0:
                return print("Помилка! Матриця вироджена, LUP-розклад неможливий.")
            self.matrix[k], self.matrix[kk] = self.matrix[kk], self.matrix[k]
            P[k], P[kk] = P[kk], P[k]
            for i in range(k + 1, self.size):
                self.matrix[i][k] = self.matrix[i][k] / self.matrix[k][k]
                for j in range(k + 1, self.size):
                    self.matrix[i][j] = self.matrix[i][j] - self.matrix[i][k] * self.matrix[k][j]
        return Matrix(P)

    def solve_system(self, vector: Vector):
        P = self.lup()
        Pb = [0] * self.size
        for i in range(self.size):
            Pb[i] = 0
            for j in range(self.size):
                Pb[i] = Pb[i] + P.matrix[i][j] * vector.vector[j]

        y = [0] * self.size
        for i in range(self.size):
            y[i] = Pb[i]
            for j in range(i):
                y[i] = y[i] - self.matrix[i][j] * y[j]

        x = [0] * self.size
        for i in reversed(range(self.size)):
            x[i] = y[i]
            for j in range(i + 1, self.size):
                x[i] = x[i] - self.matrix[i][j] * x[j]
            x[i] = x[i] / self.matrix[i][i]
        return x

    def print_matrix(self):
        matrix = ""
        for row in self.matrix:
            matrix = matrix + str(row) + "\n"
        return matrix


class Vector:
    def __init__(self, vector):
        self.vector = vector
        self.size = len(vector)

    def add_vector(self, other):
        result = []
        for i in range(self.size):
            result.append(self.vector[i] + other.vector[i])
        return Vector(result)

    def sub_vector(self, other):
        result = []
        for i in range(self.size):
            result.append(self.vector[i] - other.vector[i])
        return Vector(result)

    def mul_vector(self, other):
        result = 0
        for i in range(self.size):
            result = result + self.vector[i] * other.vector[i]
        return result

    def print_vector(self):
        return str(self.vector)


"""M1 = Matrix([
    [9, -3, 2, -9, -10],
    [5, -5, 2, -2, 7],
    [3, 5, 3, -8, 2],
    [3, -5, 6, 1, 8],
    [8, -4, -8, 5, -3]
])

M2 = Matrix([
    [7, 2, -3, 8, -1],
    [5, 3, 0, -2, -7],
    [11, 5, -4, -8, 1],
    [9, -1, 6, -2, 8],
    [-2, -4, 1, 10, -3]
])

V = Vector([1, 7, -3, 11, 5])

sum = M1.add_matrix(M2)
sub = M1.sub_matrix(M2)
mul = M1.mul_matrix(M2)
mul_v = M1.mul_vector(V)
print("Сума матриць М1 + М2: \n", sum.print_matrix(), "\n")
print("Різнииця матриць М1 - М2: \n", sub.print_matrix(), "\n")
print("Добуток матриць М1 * М2: \n", mul.print_matrix(), "\n")
print("Добуток матриці на вектор М1 * V: \n", mul_v, "\n")"""


A = Matrix([
    [9, -3, 2, -9, -10, -6],
    [5, -5, 2, -2, 7, -2],
    [3, 5, 3, -8, 2, -8],
    [3, -5, 6, 1, 8, 0],
    [8, -4, -8, 5, -3, 8],
    [4, 0, -3, 0, -2, -3]
])

B = Vector([9, 10, 9, -5, -10, -6])
X = A.solve_system(B)
print("А * Х = В, де Х дорівнює: ", X)