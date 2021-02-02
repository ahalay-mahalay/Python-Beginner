# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class MyDivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


a = 0
try:
    if a == 0:
        raise MyDivisionByZero("You divide by Zero!")
except MyDivisionByZero as err:
    print(err)
else:
    print(123 / a)
