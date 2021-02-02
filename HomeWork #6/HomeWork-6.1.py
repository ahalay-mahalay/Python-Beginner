# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import time
import colorama

colorama.init()


class TrafficLight:
    __color = {"red": [colorama.Fore.RED, 7],
               "yellow": [colorama.Fore.YELLOW, 2],
               "green": [colorama.Fore.GREEN, 7]}

    def running(self):
        try:
            if list(self.__color.keys()).index("red") == 0 \
                    and self.__color["red"][0] == colorama.Fore.RED \
                    and list(self.__color.keys()).index("yellow") == 1 \
                    and self.__color["yellow"][0] == colorama.Fore.YELLOW \
                    and list(self.__color.keys()).index("green") == 2 \
                    and self.__color["green"][0] == colorama.Fore.GREEN:
                for key, value in self.__color.items():
                    print(f"\r{value[0]}{key}", colorama.Style.RESET_ALL, end="")
                    time.sleep(value[1])
            else:
                print(f"{colorama.Fore.LIGHTYELLOW_EX}Wrong attribute!{colorama.Style.RESET_ALL}")
        except ValueError:
            print(f"{colorama.Fore.LIGHTYELLOW_EX}Wrong order!{colorama.Style.RESET_ALL}")


traffic_light_1 = TrafficLight()
traffic_light_1.running()
