# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    _income = {"wage": 25000, "bonus": 10000}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def get_full_name(self):
        print(f"Worker: {self.name} {self.surname}, {self.position}")

    def get_total_income(self):
        total_income = 0
        for key, value in super()._income.items():
            total_income += value
        print(f"Total income: {total_income}")


worker_1 = Position("Patrik", "Pinky", "worker")
worker_1.get_full_name()
worker_1.get_total_income()

ceo = Position("Sponge", "Brain", "CEO")
Worker._income = {"wage": 3500, "bonus": 700000}
ceo.get_full_name()
ceo.get_total_income()
