# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#
# Примеры матриц вы найдете в методичке.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно
# — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
from random import randint


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join("\t".join([str(item) for item in line]) for line in self.matrix)

    def __add__(self, other):
        try:
            m = [
                [int(self.matrix[line][item]) + int(other.matrix[line][item]) for item in range(len(self.matrix[line]))]
                for line in range(len(self.matrix))]
            return Matrix(m)
        except IndexError:
            return "Error: Matrix sizes do not match."


# Matrix generator
def gen_matrix(w, h):
    return [[randint(1, 9) for _ in range(w)] for _ in range(h)]


# matrix size
width = 3
height = 3

matrix_1 = Matrix(gen_matrix(width, height))
matrix_2 = Matrix(gen_matrix(width, height))
matrix_3 = Matrix(gen_matrix(width, height))
print(matrix_1, matrix_2, sep="\n")
print(matrix_1 + matrix_2)
