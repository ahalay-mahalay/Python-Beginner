# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} goes!")

    def stop(self):
        print(f"{self.name} stops!")

    def turn(self, direction):
        print(f"{self.name} turned {direction}!")

    def show_speed(self):
        print(f"Current speed is {self.speed}")


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f"{self.name} exceeded speed by {self.speed - self.speed_limit}!")
        super().show_speed()


class SportCar(Car):
    def show_speed(self):
        print("- Why are all these cars standing on the road?")
        super().show_speed()


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f"{self.name} exceeded speed by {self.speed - self.speed_limit}!")
        super().show_speed()


class PoliceCar(Car):
    def show_speed(self):
        print("- Turn on the flasher and relax!")
        super().show_speed()


town_car = TownCar(50, "blue-green in yellow specks", "Lyuda Zubilo")
sport_car = SportCar(150, "yellow with black stripes", "Chelovert Comarex")
work_car = WorkCar(30, "just big yellow machine", "Dogerpillar")
police_car = PoliceCar(90, "white with blue stripe", "Lord Ficus", True)

town_car.go()
town_car.turn("left")
town_car.show_speed()
town_car.speed = 87
town_car.show_speed()
town_car.stop()
print("-" * 46)
sport_car.go()
sport_car.turn("right")
sport_car.show_speed()
sport_car.stop()
print("-" * 46)
work_car.go()
work_car.turn("left")
work_car.show_speed()
work_car.speed = 69
work_car.show_speed()
work_car.stop()
print("-" * 46)
police_car.go()
police_car.turn("right")
police_car.show_speed()
police_car.stop()
