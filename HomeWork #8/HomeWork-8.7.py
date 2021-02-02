# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
# и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        z = [self.real + other.real,
             self.imaginary + other.imaginary]
        sign = ""
        if z[1] >= 0:
            sign = "+"
        return complex(f"{z[0]}{sign}{z[1]}j")

    def __mul__(self, other):
        z = [self.real * other.real - self.imaginary * other.imaginary,
             self.real * other.imaginary + other.real * self.imaginary]
        sign = ""
        if z[1] >= 0:
            sign = "+"
        return complex(f"{z[0]}{sign}{z[1]}j")


a = ComplexNumber(-2, 3)
b = ComplexNumber(4, -7)
c = a + b
d = a * b
print(c)
print(d)
print(c + d)
print(c * d)
